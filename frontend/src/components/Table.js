import { useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api';

function Table({ links, onLinkDeleted }) {
  const [search, setSearch] = useState('');
  const filteredLinks = links.filter(link =>
    link.target_url.includes(search) || link.code.includes(search)
  );

  const handleDelete = async (code) => {
    if (window.confirm('Are you sure?')) {
      try {
        await api.deleteLink(code);
        onLinkDeleted(code);
      } catch (err) {
        alert('Error deleting link');
      }
    }
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    alert('Copied to clipboard');
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-4">Your Links</h2>
      <input
        type="text"
        placeholder="Search..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full p-2 border rounded mb-4"
      />
      <div className="overflow-x-auto">
        <table className="w-full table-auto">
          <thead>
            <tr className="bg-gray-50">
              <th className="p-2 text-left">Code</th>
              <th className="p-2 text-left">Target URL</th>
              <th className="p-2 text-left">Clicks</th>
              <th className="p-2 text-left">Last Clicked</th>
              <th className="p-2 text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredLinks.map(link => (
              <tr key={link.code} className="border-t">
                <td className="p-2">{link.code}</td>
                <td className="p-2 truncate max-w-xs" title={link.target_url}>{link.target_url}</td>
                <td className="p-2">{link.clicks}</td>
                <td className="p-2">{link.last_clicked ? new Date(link.last_clicked).toLocaleString() : 'Never'}</td>
                <td className="p-2">
                  <button onClick={() => copyToClipboard(link.short_url)} className="text-blue-500 mr-2">Copy</button>
                  <Link to={`/${link.code}`} className="text-green-500 mr-2">Stats</Link>
                  <button onClick={() => handleDelete(link.code)} className="text-red-500">Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Table;
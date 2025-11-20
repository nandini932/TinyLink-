import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { api } from '../api';

function Stats() {
  const { code } = useParams();
  const [link, setLink] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchStats();
  }, [code]); // eslint-disable-line react-hooks/exhaustive-deps

  const fetchStats = async () => {
    try {
      const response = await api.getLinkStats(code);
      setLink(response.data);
    } catch (err) {
      setError('Link not found');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="text-center mt-10">Loading...</div>;

  if (error) return <div className="text-center mt-10 text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-8">Link Stats</h1>
      <div className="bg-white p-6 rounded-lg shadow-md max-w-2xl mx-auto">
        <p><strong>Code:</strong> {link.code}</p>
        <p><strong>Target URL:</strong> <a href={link.target_url} className="text-blue-500" target="_blank" rel="noopener noreferrer">{link.target_url}</a></p>
        <p><strong>Short URL:</strong> <a href={link.short_url} className="text-blue-500" target="_blank" rel="noopener noreferrer">{link.short_url}</a></p>
        <p><strong>Clicks:</strong> {link.clicks}</p>
        <p><strong>Last Clicked:</strong> {link.last_clicked ? new Date(link.last_clicked).toLocaleString() : 'Never'}</p>
        <p><strong>Created At:</strong> {new Date(link.created_at).toLocaleString()}</p>
      </div>
      <div className="text-center mt-4">
        <Link to="/" className="text-blue-500">Back to Dashboard</Link>
      </div>
    </div>
  );
}

export default Stats;
import { useState } from 'react';
import { api } from '../api';

function LinkForm({ onLinkCreated }) {
  const [targetUrl, setTargetUrl] = useState('');
  const [code, setCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const response = await api.createLink({
        target_url: targetUrl,
        code: code || undefined
      });
      onLinkCreated(response.data);
      setTargetUrl('');
      setCode('');
    } catch (err) {
      setError(err.response?.data?.error || 'Error creating link');
    } finally {
      setLoading(false);
    };
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md mb-6">
      <h2 className="text-xl font-bold mb-4">Create Short Link</h2>
      <div className="mb-4">
        <label className="block text-sm font-medium mb-2">Target URL</label>
        <input
          type="url"
          value={targetUrl}
          onChange={(e) => setTargetUrl(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium mb-2">Custom Code (optional)</label>
        <input
          type="text"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className="w-full p-2 border rounded"
          pattern="[A-Za-z0-9]{6,8}"
        />
      </div>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
      >
        {loading ? 'Creating...' : 'Create Link'}
      </button>
    </form>
  );
}

export default LinkForm;

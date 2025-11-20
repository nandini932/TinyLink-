import { useState, useEffect } from 'react';
import LinkForm from './LinkForm';
import Table from './Table';
import { api } from '../api';

function Dashboard() {
  const [links, setLinks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLinks();
  }, []);

  const fetchLinks = async () => {
    try {
      const response = await api.getLinks();
      setLinks(response.data);
    } catch (err) {
      console.error('Error fetching links', err);
    } finally {
      setLoading(false);
    }
  };

  const handleLinkCreated = (newLink) => {
    setLinks([newLink, ...links]);
  };

  const handleLinkDeleted = (code) => {
    setLinks(links.filter(link => link.code !== code));
  };

  if (loading) return <div className="text-center mt-10">Loading...</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-8">TinyLink Dashboard</h1>
      <LinkForm onLinkCreated={handleLinkCreated} />
      <Table links={links} onLinkDeleted={handleLinkDeleted} />
    </div>
  );
}

export default Dashboard;
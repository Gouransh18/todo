'use client';

import { useEffect, useState } from 'react';

interface Profile {
  id: number;
  name: string;
  email: string;
  role: string;
}

export default function DashboardPage() {
  const [profiles, setProfiles] = useState<Profile[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchProfiles() {
      try {
        const response = await fetch('http://localhost:8000/api/profiles');
        const data = await response.json();
        setProfiles(data.profiles);
      } catch (error) {
        console.error('Error fetching profiles:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchProfiles();
  }, []);

  if (loading) {
    return <div className="flex justify-center items-center min-h-screen">Loading...</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>
      
      <div className="bg-white rounded-lg shadow">
        <div className="p-6">
          <h2 className="text-xl font-semibold mb-4">Profiles</h2>
          <div className="grid gap-4">
            {profiles.map((profile) => (
              <div key={profile.id} className="border p-4 rounded-lg">
                <h3 className="font-medium">{profile.name}</h3>
                <p className="text-gray-600">{profile.email}</p>
                <span className="text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded">
                  {profile.role}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
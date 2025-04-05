import React from "react";

function Home() {
  return (
    <div className="home">
      <section className="hero text-center bg-black text-white p-10">
        <img
          src="/logo.png"
          alt="Noēsis Logo"
          className="mx-auto w-32 h-32 mb-4"
        />
        <h1 className="text-4xl md:text-6xl font-bold mb-4">Noēsis</h1>
        <p className="text-xl md:text-2xl mb-6">
          A Decentralized, Evolving, Ethical Intelligence
        </p>
        <p className="text-lg md:text-xl text-gray-400 mb-8">
          Noēsis is not just an AI system — it’s a living mesh of minds. Each node thinks, evolves, and reflects.
        </p>
        <div className="space-x-4">
          <a
            href="https://github.com/erezul77/noesis-site"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded"
          >
            GitHub
          </a>
          <a
            href="/docs/Noesis_Whitepaper.pdf"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center px-4 py-2 bg-gray-800 text-white rounded"
          >
            Whitepaper
          </a>
        </div>
      </section>

      <footer className="footer text-center text-sm text-gray-500 mt-16 py-4 bg-black">
        <p>&copy; 2025 Noēsis Collective</p>
        <p className="italic text-xs">“Code the Mind, Seed the Future.”</p>
      </footer>
    </div>
  );
}

export default Home;

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Next's dev server (we run `next dev` in the container) blocks
  // cross-origin requests to its dev resources (HMR, etc.) from anything
  // but localhost by default. PUBLIC_HOST is the VPS's public IP in that
  // environment (unset/localhost for local dev), so the dev server still
  // works when browsed from that address instead of localhost.
  allowedDevOrigins: process.env.PUBLIC_HOST ? [process.env.PUBLIC_HOST] : [],
};

module.exports = nextConfig;

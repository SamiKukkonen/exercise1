const express = require('express');
const os = require('os');
const { execSync } = require('child_process');

const app = express();
const PORT = 3000;

function getSystemInfo() {
  // Get IP address
  const networkInterfaces = os.networkInterfaces();
  const ipAddress = networkInterfaces.eth0 ? networkInterfaces.eth0[0].address : 'N/A';

  // Get list of running processes
  const processes = execSync('ps ax').toString();

  // Get available disk space
  const diskSpace = execSync('df -h /').toString();

  // Get time since last boot
  const bootTime = execSync('uptime -s').toString().trim();

  return {
    ip_address: ipAddress,
    processes: processes,
    disk_space: diskSpace,
    boot_time: bootTime
  };
}

app.get('/', (req, res) => {
  res.json(getSystemInfo());
});

app.listen(PORT, () => {
  console.log(`Service 2 running on port ${PORT}`);
});


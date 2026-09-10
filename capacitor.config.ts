import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.convertflow.app',
  appName: 'ConvertFlow',
  webDir: 'dist',
  server: {
    androidScheme: 'https',
    url: 'https://convertflow-seven-delta.vercel.app/',
    cleartext: false,
  },
};

export default config;

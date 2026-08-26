import React, { useState, useEffect } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import LightModeIcon from '@mui/icons-material/LightMode';
import Dashboard from './components/Dashboard';
import AccountList from './components/AccountList';
import TweetFeed from './components/TweetFeed';
import StatsCard from './components/StatsCard';
import { WebSocketProvider } from './context/WebSocketContext';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#1DA1F2',
    },
    background: {
      default: '#15202B',
      paper: '#192734',
    },
  },
});

const lightTheme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1DA1F2',
    },
    background: {
      default: '#FFFFFF',
      paper: '#F5F8FA',
    },
  },
});

function App() {
  const [darkMode, setDarkMode] = useState(true);
  const [accounts, setAccounts] = useState([]);
  const [selectedAccount, setSelectedAccount] = useState(null);
  const [tweets, setTweets] = useState([]);
  const [stats, setStats] = useState({
    totalAccounts: 0,
    totalTweets: 0,
    totalMentions: 0,
    totalEngagement: 0,
  });

  useEffect(() => {
    // Fetch accounts from backend
    fetchAccounts();
    
    // WebSocket connection
    const ws = new WebSocket('ws://localhost:8000/ws/dashboard');
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      handleWebSocketMessage(data);
    };
    
    return () => {
      ws.close();
    };
  }, []);

  const fetchAccounts = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/accounts');
      const data = await response.json();
      setAccounts(data);
    } catch (error) {
      console.error('Failed to fetch accounts:', error);
    }
  };

  const handleWebSocketMessage = (data) => {
    switch (data.type) {
      case 'new_tweet':
        setTweets(prev => [data.tweet, ...prev]);
        break;
      case 'mention':
        // Update mentions
        break;
      case 'stats_update':
        setStats(data.stats);
        break;
      default:
        break;
    }
  };

  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  return (
    <ThemeProvider theme={darkMode ? darkTheme : lightTheme}>
      <CssBaseline />
      <WebSocketProvider>
        <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
          <AppBar position="static" color="transparent" elevation={1}>
            <Toolbar>
              <Typography variant="h6" sx={{ flexGrow: 1, fontWeight: 'bold' }}>
                🐦 X Account Dashboard
              </Typography>
              <IconButton onClick={toggleTheme} color="inherit">
                {darkMode ? <LightModeIcon /> : <DarkModeIcon />}
              </IconButton>
            </Toolbar>
          </AppBar>
          
          <Container maxWidth="xl" sx={{ mt: 3, flex: 1 }}>
            <Box sx={{ display: 'grid', gridTemplateColumns: '300px 1fr', gap: 3 }}>
              {/* Left sidebar - Account List */}
              <Box>
                <AccountList
                  accounts={accounts}
                  selectedAccount={selectedAccount}
                  onSelectAccount={setSelectedAccount}
                  onAddAccount={() => {
                    // Add account dialog
                  }}
                />
              </Box>
              
              {/* Main content */}
              <Box>
                <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 2, mb: 3 }}>
                  <StatsCard
                    title="Total Accounts"
                    value={stats.totalAccounts}
                    icon="👤"
                    color="#1DA1F2"
                  />
                  <StatsCard
                    title="Tweets Tracked"
                    value={stats.totalTweets}
                    icon="📝"
                    color="#17BF63"
                  />
                  <StatsCard
                    title="Mentions"
                    value={stats.totalMentions}
                    icon="🔔"
                    color="#F45D22"
                  />
                  <StatsCard
                    title="Engagement"
                    value={stats.totalEngagement}
                    icon="❤️"
                    color="#E0245E"
                  />
                </Box>
                
                <TweetFeed
                  tweets={tweets}
                  selectedAccount={selectedAccount}
                />
              </Box>
            </Box>
          </Container>
        </Box>
      </WebSocketProvider>
    </ThemeProvider>
  );
}

export default App;
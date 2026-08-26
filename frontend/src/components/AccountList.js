// frontend/src/components/AccountList.js

import React, { useState } from 'react';
import {
  List,
  ListItem,
  ListItemAvatar,
  ListItemText,
  Avatar,
  Chip,
  Box,
  Button,
  TextField,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Typography,
  CircularProgress,
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import RefreshIcon from '@mui/icons-material/Refresh';

function AccountList({ accounts, selectedAccount, onSelectAccount, onAddAccount }) {
  const [dialogOpen, setDialogOpen] = useState(false);
  const [newUsername, setNewUsername] = useState('');
  const [loading, setLoading] = useState(false);

  const handleAddAccount = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/accounts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: newUsername }),
      });
      
      if (response.ok) {
        const account = await response.json();
        onAddAccount(account);
        setDialogOpen(false);
        setNewUsername('');
      }
    } catch (error) {
      console.error('Failed to add account:', error);
    }
    setLoading(false);
  };

  const handleRefresh = async () => {
    // Refresh all accounts
    try {
      await fetch('http://localhost:8000/api/accounts/refresh', {
        method: 'POST',
      });
    } catch (error) {
      console.error('Failed to refresh:', error);
    }
  };

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2, alignItems: 'center' }}>
        <Typography variant="h6">Accounts</Typography>
        <Box>
          <Button
            size="small"
            onClick={handleRefresh}
            startIcon={<RefreshIcon />}
            sx={{ mr: 1 }}
          >
            Refresh
          </Button>
          <Button
            variant="contained"
            size="small"
            startIcon={<AddIcon />}
            onClick={() => setDialogOpen(true)}
          >
            Add
          </Button>
        </Box>
      </Box>

      <List>
        {accounts.map((account) => (
          <ListItem
            key={account.id}
            button
            selected={selectedAccount?.id === account.id}
            onClick={() => onSelectAccount(account)}
            sx={{
              borderRadius: 1,
              mb: 1,
              '&.Mui-selected': {
                backgroundColor: 'primary.main',
                '&:hover': {
                  backgroundColor: 'primary.dark',
                },
              },
            }}
          >
            <ListItemAvatar>
              <Avatar
                src={account.avatar_url}
                alt={account.username}
                sx={{
                  width: 40,
                  height: 40,
                  border: account.is_verified ? '2px solid #1DA1F2' : 'none',
                }}
              />
            </ListItemAvatar>
            <ListItemText
              primary={
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Typography variant="body1" fontWeight="medium">
                    {account.username}
                  </Typography>
                  {account.is_verified && (
                    <Chip
                      label="✓"
                      size="small"
                      sx={{
                        bgcolor: '#1DA1F2',
                        color: 'white',
                        height: 20,
                        fontSize: 12,
                      }}
                    />
                  )}
                </Box>
              }
              secondary={`${account.followers_count} followers • ${account.tweet_count} tweets`}
            />
          </ListItem>
        ))}
      </List>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)}>
        <DialogTitle>Add X Account</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Username"
            fullWidth
            value={newUsername}
            onChange={(e) => setNewUsername(e.target.value)}
            placeholder="elonmusk"
            variant="outlined"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setDialogOpen(false)}>Cancel</Button>
          <Button
            onClick={handleAddAccount}
            variant="contained"
            disabled={loading || !newUsername}
          >
            {loading ? <CircularProgress size={24} /> : 'Add Account'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default AccountList;
// frontend/src/components/TweetFeed.js

import React from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Avatar,
  Chip,
  IconButton,
  Stack,
  Divider,
} from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import RepeatIcon from '@mui/icons-material/Repeat';
import ChatBubbleOutlineIcon from '@mui/icons-material/ChatBubbleOutline';
import BarChartIcon from '@mui/icons-material/BarChart';
import { formatDistanceToNow } from 'date-fns';

function TweetFeed({ tweets, selectedAccount }) {
  const filteredTweets = selectedAccount
    ? tweets.filter(t => t.account_id === selectedAccount.id)
    : tweets;

  return (
    <Box>
      <Typography variant="h6" sx={{ mb: 2 }}>
        {selectedAccount ? `@${selectedAccount.username}'s Tweets` : 'Live Feed'}
      </Typography>
      
      <Stack spacing={2}>
        {filteredTweets.map((tweet) => (
          <Card key={tweet.id} variant="outlined">
            <CardContent>
              <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 2 }}>
                <Avatar
                  src={tweet.avatar_url}
                  alt={tweet.username}
                  sx={{ width: 48, height: 48 }}
                />
                <Box sx={{ flex: 1 }}>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                    <Typography variant="subtitle1" fontWeight="bold">
                      {tweet.display_name}
                    </Typography>
                    <Typography variant="caption" color="text.secondary">
                      @{tweet.username}
                    </Typography>
                    <Typography variant="caption" color="text.secondary">
                      ·
                    </Typography>
                    <Typography variant="caption" color="text.secondary">
                      {formatDistanceToNow(new Date(tweet.created_at), { addSuffix: true })}
                    </Typography>
                  </Box>
                  
                  <Typography variant="body1" sx={{ mt: 1, whiteSpace: 'pre-wrap' }}>
                    {tweet.content}
                  </Typography>
                  
                  {tweet.media && tweet.media.length > 0 && (
                    <Box sx={{ mt: 2, display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 1 }}>
                      {tweet.media.map((media, index) => (
                        <Box
                          key={index}
                          component="img"
                          src={media.preview}
                          alt="Tweet media"
                          sx={{
                            width: '100%',
                            borderRadius: 1,
                            maxHeight: 200,
                            objectFit: 'cover',
                          }}
                        />
                      ))}
                    </Box>
                  )}
                  
                  <Box sx={{ display: 'flex', justifyContent: 'space-around', mt: 2, pt: 1 }}>
                    <IconButton size="small">
                      <ChatBubbleOutlineIcon fontSize="small" />
                      <Typography variant="caption" sx={{ ml: 0.5 }}>
                        {tweet.replies}
                      </Typography>
                    </IconButton>
                    <IconButton size="small">
                      <RepeatIcon fontSize="small" />
                      <Typography variant="caption" sx={{ ml: 0.5 }}>
                        {tweet.retweets}
                      </Typography>
                    </IconButton>
                    <IconButton size="small">
                      <FavoriteIcon fontSize="small" />
                      <Typography variant="caption" sx={{ ml: 0.5 }}>
                        {tweet.likes}
                      </Typography>
                    </IconButton>
                    <IconButton size="small">
                      <BarChartIcon fontSize="small" />
                      <Typography variant="caption" sx={{ ml: 0.5 }}>
                        {tweet.views}
                      </Typography>
                    </IconButton>
                  </Box>
                </Box>
              </Box>
            </CardContent>
          </Card>
        ))}
        
        {filteredTweets.length === 0 && (
          <Card variant="outlined">
            <CardContent>
              <Typography color="text.secondary" align="center">
                No tweets available
              </Typography>
            </CardContent>
          </Card>
        )}
      </Stack>
    </Box>
  );
}

export default TweetFeed;
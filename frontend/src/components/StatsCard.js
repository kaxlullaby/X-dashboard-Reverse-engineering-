// frontend/src/components/StatsCard.js

import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';

function StatsCard({ title, value, icon, color }) {
  return (
    <Card variant="outlined">
      <CardContent>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Box>
            <Typography variant="caption" color="text.secondary">
              {title}
            </Typography>
            <Typography variant="h4" sx={{ mt: 1 }}>
              {value.toLocaleString()}
            </Typography>
          </Box>
          <Box
            sx={{
              bgcolor: `${color}20`,
              borderRadius: '50%',
              p: 1,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <Typography variant="h5" sx={{ color }}>
              {icon}
            </Typography>
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
}

export default StatsCard;
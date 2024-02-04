import { AppBar, Box, Button, Container, CssBaseline, Toolbar, Typography, colors } from "@mui/material";
import React from "react";
import LoginIcon from '@mui/icons-material/Login';
import { Link } from "react-router-dom";

export const HomePage = () => {
	return (
		<React.Fragment>
			<CssBaseline />

			<Container style={{display: "flex", flexDirection: "column", justifyContent: "space-between"}}>
				<Typography variant="h3" component="h3" gutterBottom style={{margin: "30px"}}>
					Welcome to Destination Bucket List! 
				</Typography>
                <Typography variant="h5" component="h5" gutterBottom style={{margin: "15px"}}>
                    Please login to continue.
                </Typography>
                <Box sx={{ flexGrow: 1, margin: "20px" }}>
			        <AppBar position="static" sx={{ marginBottom: "20px", backgroundColor: colors.red[500] }}>
                    <Toolbar sx={{display: "flex", flexDirection: "row", justifyContent: "space-evenly"}}>
                        <Button
                            to="/user-login"
                            component={Link}
                            color="inherit"
                            sx={{ mr: 5 }}
                            startIcon={<LoginIcon />}
                            > 
                            User Login
                        </Button>
                        <Button 
                            to="/admin-login" 
                            component={Link}
                            color="inherit"
                            sx={{ mr: 5 }}
                            startIcon={<LoginIcon />}>
                            Admin Login
                        </Button>
				    </Toolbar>
                    </AppBar>
                </Box>
			</Container>
		</React.Fragment>
	);
};
import { AppBar, Box, Button, Container, Toolbar, Typography, colors, TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from "@mui/material";
import { useEffect, useState } from "react";
import { BACKEND_URL } from "../utils";
import { Link, useLocation } from "react-router-dom";
import AddIcon from '@mui/icons-material/Add';
import LogoutIcon from '@mui/icons-material/Logout';


export const AdminPage = () => {
    const [loading, setLoading] = useState(false);
    const [destinations, setDestinations] = useState([])
    const location = useLocation();
	const path = location.pathname;

    useEffect(() => {
        setLoading(true);
        fetch(`${BACKEND_URL}/public_list/`)
        .then(response => response.json())
        .then(data => { setDestinations(data.destination); setLoading(false); });
    }, []);

    return (
        <Container>
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static" sx={{ marginBottom: "40px", backgroundColor: colors.red[500] }}>
                <Toolbar>
                    <Button
                        to="/"
                        component={Link}
                        color="inherit"
                        sx={{ mr: 2, marginRight: "140px" }}
                        startIcon={<LogoutIcon />}>
                        Logout
                    </Button>
                    <Typography variant="h6" component="div" sx={{ mr: 5 }}>
                        Destination Bucket List Management
                    </Typography>
                    
                    <Button
                        variant={path.startsWith("/destinations/add") ? "outlined" : "text"}
                        to="/destinations/add"
                        component={Link}
                        color="inherit"
                        sx={{ mr: 4 }}
                        startIcon={<AddIcon />}>
                        Add Destination
                    </Button>
                </Toolbar>
                </AppBar>
            </Box>

            <h2>Destination Public List</h2>
            {!loading && destinations.length === 0 && <div>No destinations in the list</div>}
            {!loading && destinations.length > 0 && (
                <>
                <TableContainer style={{backgroundColor: colors.grey[100]}}>
                    <Table sx={{ minWidth: 850, maxWidth: 1200}} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell align="center">#</TableCell>
                                <TableCell align="center">Title</TableCell>
                                <TableCell align="center">Geolocation</TableCell>
                                <TableCell align="center">Image</TableCell>
                                <TableCell align="center">Description</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {destinations.map((destination: any, index: number) => (
                                <TableRow key={destination.id}>
                                    <TableCell align="center" component="th" scope="row">{index + 1}</TableCell>
                                    <TableCell align="center" component="th" scope="row">{destination.title}</TableCell>
                                    <TableCell align="center">{destination.geolocation}</TableCell>
                                    <TableCell align="center">{destination.image}</TableCell>
                                    <TableCell align="center">{destination.description}</TableCell>
                                </TableRow>
                                ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                </>
                
            )}
        </Container>
    );
}

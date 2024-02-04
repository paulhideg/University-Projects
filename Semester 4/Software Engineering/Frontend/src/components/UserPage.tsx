import { AppBar, Box, Button, Container, Toolbar, Typography, colors, TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from "@mui/material";
import { useEffect, useState } from "react";
import { BACKEND_URL } from "../utils";
import { Link, useLocation, useParams } from "react-router-dom";
import AddIcon from '@mui/icons-material/Add';
import LogoutIcon from '@mui/icons-material/Logout';
import AddBoxIcon from '@mui/icons-material/AddBox';
import { SESSION_ID } from "./AppUserLogin";


export const UserPage = () => {
    const [loading, setLoading] = useState(false);
    const [publicList, setPublicList] = useState([]);
    const [bucketList, setBucketList] = useState([]);
    const location = useLocation();
	const path = location.pathname;
    
    useEffect(() => {
        setLoading(true);
        fetch(`${BACKEND_URL}/public_list/`)
        .then(response => response.json())
        .then(data => { setPublicList(data.destination); setLoading(false); });
    }, []);

    useEffect(() => {
        setLoading(true);
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ session_id: sessionStorage.getItem("id") }), 
          };
        
          fetch(`${BACKEND_URL}/user/list/`, requestOptions)
            .then((response) => response.json())
            .then((data) => {
              setBucketList(data.destination);
              setLoading(false);
              console.log(data);
            });
    }, []);

    return (
        <div style={{ height: "100%", width: "100%", display: "flex", justifyContent: "center" }}>
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
                    <Typography variant="h6" component="div" sx={{ mr: 5, marginRight: "60px" }}>
                        Destination Bucket List
                    </Typography>
                    
                    <Button
                        variant={path.startsWith("/destinations/add-new-destination") ? "outlined" : "text"}
                        to="/destinations/add-new-destination"
                        component={Link}
                        color="inherit"
                        sx={{ mr: 4 }}
                        startIcon={<AddIcon />}>
                        Add New Destination
                    </Button>
                    <Button
                        variant={path.startsWith("/destinations/add-public-destination") ? "outlined" : "text"}
                        to="/destinations/add-public-destination"
                        component={Link}
                        color="inherit"
                        sx={{ mr: 4 }}
                        startIcon={<AddBoxIcon />}>
                        Add Destination From Public List
                    </Button>
                </Toolbar>
                </AppBar>
            </Box>

            <h3>Destination Public List</h3>
            {!loading && publicList.length === 0 && <div>No destinations in the public list</div>}
            {!loading && publicList.length > 0 && (
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
                            {publicList.map((destination: any, index: number) => (
                                <TableRow key={destination.id}>
                                    <TableCell align="center" component="th" scope="row">{index + 1}</TableCell>
                                    <TableCell align="center" component="th" scope="row">{destination.title}</TableCell>
                                    <TableCell align="center">{destination.geolocation}</TableCell>
                                    <TableCell align="center">
                                    <a href={destination.image} style={{ textDecoration: 'underline' }}>
                                        {destination.image}
                                    </a>
                                    </TableCell>
                                    <TableCell align="center">{destination.description}</TableCell>
                                </TableRow>
                                ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                </>    
            )}

            <h3 style={{marginTop: "50px"}}>My Bucket List</h3>
            {!loading && bucketList.length === 0 && <div>No destinations in the bucket list</div>}
            {!loading && bucketList.length > 0 && (
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
                                <TableCell align="center">Stay Dates</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {bucketList.map((destination: any, index: number) => (
                                <TableRow key={destination.id}>
                                    <TableCell align="center" component="th" scope="row">{index + 1}</TableCell>
                                    <TableCell align="center" component="th" scope="row">{destination.title}</TableCell>
                                    <TableCell align="center">{destination.geolocation}</TableCell>
                                    <TableCell align="center">{destination.image}</TableCell>
                                    <TableCell align="center">{destination.description}</TableCell>
                                    <TableCell align="center">{destination.start_date} {"->"} {destination.end_date}</TableCell>
                                </TableRow>
                                ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                </>    
            )}

        </Container>
        </div>
        
    );
}
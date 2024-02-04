import { Button, Card, CardContent, Container, FormLabel, TextField, colors, IconButton } from "@mui/material";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { User } from "../models/User";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { BACKEND_URL } from "../utils";


export var SESSION_ID = "";

export const AppUserLogin = () => {
    const navigate = useNavigate();
    const [, setSubmitting] = useState(false);
    const [, setOpen] = useState(false);

    const [user, setUser] = useState<User>({
        id: 1,
        username: '',
        password: '', 
        role: 'user',
    });

    
    
    const appLogin = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        setSubmitting(true);
        try {
            const response = await fetch(`${BACKEND_URL}/login/`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(user),
            });
            const data = await response.json();
            sessionStorage.setItem("id", data.session_id);
            // SESSION_ID = data.session_id;
            if (response.ok) {
                setOpen(true);
                navigate("/user-page");
                alert("Logged in successfully");
            }
            else {
                setOpen(true);
                alert("Invalid username or password");
            }
        }
        catch (error) {
            console.log(error);
            alert("Failed to login");
        }    
        setSubmitting(false);
    }

    return (
        <Container>
            <Card>
                <CardContent style={{width: "700px"}}>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/`}>
						<ArrowBackIcon />
					</IconButton>{" "}
                    <form onSubmit={appLogin} style={{display: "flex", flexDirection: "column", padding: "8px", alignItems: "center"}}>
                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Username
                            </FormLabel>
                            <TextField onChange={(event) => setUser({ ...user, username: event.target.value })}
                                id='username'
                                variant="outlined"
                            >    
                            </TextField>
                        </Container>
                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Password
                            </FormLabel>
                            <TextField onChange={(event) => setUser({ ...user, password: event.target.value })}
                                id='username'
                                variant="outlined"
                                // set type to password
                                type="password"
                            >    
                            </TextField>
                        </Container>
                        <Button type="submit" variant="contained" sx={{ backgroundColor: colors.red[400], width: "300px", marginTop: "30px"}}>Login</Button>
                    </form>
                </CardContent>
            </Card>
        </Container>
    )
}
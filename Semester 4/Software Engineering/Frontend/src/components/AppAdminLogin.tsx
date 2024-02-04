import { Button, Card, CardContent, Container, FormLabel, TextField, colors, IconButton } from "@mui/material";
import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { User } from "../models/User";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { BACKEND_URL } from "../utils";


export const AppAdminLogin = () => {
    const navigate = useNavigate();
    const [, setSubmitting] = useState(false);
    const [, setOpen] = useState(false);

    const [admin, setAdmin] = useState<User>({
        id: 1,
        username: '',
        password: '',
        role: 'admin',
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
                body: JSON.stringify(admin),
            });
            if (response.ok) {
                setOpen(true);
                navigate("/admin-page");
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
                                Admin
                            </FormLabel>
                            <TextField onChange={(event) => setAdmin({ ...admin, username: event.target.value })}
                                id='username'
                                variant="outlined"
                                style={{marginLeft: "30px"}}
                            >    
                            </TextField>
                        </Container>
                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Password
                            </FormLabel>
                            <TextField onChange={(event) => setAdmin({ ...admin, password: event.target.value })}
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
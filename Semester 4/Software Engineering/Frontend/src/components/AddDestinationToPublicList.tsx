import { Container, Card, CardContent, TextField, FormLabel, colors, Button, CardActions } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { BACKEND_URL } from "../utils";


export const AddDestinationToPublicList = () => {
    const navigate = useNavigate();
    const [submitting, setSubmitting] = useState(false);
    const [open, setOpen] = useState(false);

    const [destination, setDestination] = useState({
        id: 1,
        title: '',
        image: '',
        geolocation: '',
        description: '',
        startDate: '',
        endDate: '',
    });

    const addDestination = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        setSubmitting(true);
        try {
            const response = await fetch(`${BACKEND_URL}/public_list/add/`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(destination),
            });
            if (response.ok) {
                setOpen(true);
                alert("Destination added successfully");
            }
            else {
                setOpen(true);
                alert("Failed to add destination");
            }
            navigate("/admin-page");
        } catch (error) {
            console.error(error);
            alert("Failed to add destination");
        }
        setSubmitting(false);
    };

    const handleCancel = (event: { preventDefault: () => void }) => {
		event.preventDefault();
		navigate("/admin-page");
	};

    return (
        <Container>
            <Card style={{display: "flex", width: "600px", height: "450px", flexDirection: "column"}}>
                <CardContent>
                    <form onSubmit={addDestination} style={{display: "flex", flexDirection: "column", padding: "8px", marginTop: "40px"}}>
                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-around"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Title
                            </FormLabel>
                            <TextField onChange={(event) => setDestination({ ...destination, title: event.target.value })}
                                id="title"
                                variant="outlined"
                            >    
                            </TextField>
                        </Container>
    

                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-around"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Image (link)
                            </FormLabel>
                            <TextField onChange={(event) => setDestination({ ...destination, image: event.target.value})}
                                id="image"
                                variant="outlined"
                            >
                            </TextField>
                        </Container>

                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-around"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Geolocation
                            </FormLabel>
                            <TextField onChange={(event) => setDestination({ ...destination, geolocation: event.target.value })}
                                id="geolocation"
                                variant="outlined"
                            >               
                            </TextField>
                        </Container>

                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-around"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Description
                            </FormLabel>
                            <TextField onChange={(event) => setDestination({ ...destination, description: event.target.value })}
                                id="description"
                                variant="outlined"
                            >               
                            </TextField>
                        </Container>

                     </form>
                </CardContent>
                <CardActions sx={{ justifyContent: "center" }}>
                    <Button onClick={addDestination} type="submit" variant="contained" sx={{ backgroundColor: colors.red[500] }}>Add destination</Button>
					<Button onClick={handleCancel} variant="contained" sx={{ backgroundColor: colors.red[500] }}>Cancel</Button>
				</CardActions>
            </Card>
        </Container>
    );
}
import { Container, Card, CardContent, TextField, FormLabel, colors, Button, CardActions } from "@mui/material";
import { useNavigate, useParams } from "react-router-dom";
import { useState } from "react";
import { BACKEND_URL } from "../utils";
import { SESSION_ID } from "./AppUserLogin";

export const AddNewDestination = () => {
    
    const navigate = useNavigate();
    const [submitting, setSubmitting] = useState(false);
    const [open, setOpen] = useState(false);

    const [destination, setDestination] = useState({
        id: 1,
        title: '',
        image: '',
        geolocation: '',
        description: '',
        start_date: '',
        end_date: '',
    });

    const addDestination = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        setSubmitting(true);
        try {
          const requestData = {
            session_id: sessionStorage.getItem("id"), // Include the session ID
          };
      
          const response = await fetch(`${BACKEND_URL}/user/add/`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            // include the session id in the request body
            body: JSON.stringify({ ...destination, ...requestData }),
          });
      
          if (response.ok) {
            setOpen(true);
            alert("Destination added successfully");
          } else {
            setOpen(true);
            alert("Failed to add destination");
          }
          navigate("/user-page");
        } catch (error) {
          console.error(error);
          alert("Failed to add destination");
        }
        setSubmitting(false);
      };

    const handleCancel = (event: { preventDefault: () => void }) => {
		event.preventDefault();
		navigate("/user-page");
	};

    return (
        <Container>
            <Card style={{display: "flex", width: "750px", height: "550px", flexDirection: "column"}}>
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

                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-around"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                Start date
                            </FormLabel>
                            <TextField onChange={(event) => setDestination({ ...destination, start_date: event.target.value })}
                                id="startDate"
                                variant="outlined"
                            >               
                            </TextField>
                        </Container>

                        <Container sx={{padding: "3px"}} style={{display: "flex", flexDirection: "row", justifyContent: "space-around"}}>
                            <FormLabel style={{marginTop: "15px", fontSize: "18px"}}>
                                End date
                            </FormLabel>
                            <TextField onChange={(event) => setDestination({ ...destination, end_date: event.target.value })}
                                id="endDate"
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
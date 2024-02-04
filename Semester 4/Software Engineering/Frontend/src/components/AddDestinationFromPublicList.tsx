import { Container, Card, CardContent, TextField, FormLabel, colors, Button, CardActions, Autocomplete } from "@mui/material";
import { useNavigate, useParams } from "react-router-dom";
import { useState, useCallback, useEffect } from "react";
import { BACKEND_URL } from "../utils";
import { Destination } from "../models/Destination";
import axios from "axios";
import { debounce } from "lodash";

export const AddDestinationFromPublicList = () => {
    const { userId } = useParams<{ userId: string }>();
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

    const [destinations, setDestinations] = useState<Destination[]>([]);

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
            body: JSON.stringify({...destination, ...requestData}),
            });
            if (response.ok) {
                setOpen(true);
                alert("Destination added successfully");
            }
            else {
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

    const fetchSuggestions = async (query: string) => {
		try {
			const response = await axios.get(
				`${BACKEND_URL}/public_list/`
			);
			const data = await response.data.destination;
			setDestinations(data);
		} catch (error) {
			console.error("Error fetching suggestions:", error);
		}
	};

    const debouncedFetchSuggestions = useCallback(debounce(fetchSuggestions, 500), []);

	useEffect(() => {
		return () => {
			debouncedFetchSuggestions.cancel();
		};
	}, [debouncedFetchSuggestions]);

    const handleInputChange = (event: any, value: any, reason: any) => {
		console.log("input", value, reason);

		if (reason === "input") {
			debouncedFetchSuggestions(value);
		}
	};

    return (
        <Container>
            <Card style={{display: "flex", width: "700px", height: "420px", flexDirection: "column"}}>

                <CardContent>
                    <form onSubmit={addDestination} style={{display: "flex", flexDirection: "column", padding: "8px", marginTop: "40px"}}>
                        <Container sx={{padding: "3px"}} style={{display: "flex", justifyContent: "space-around"}}>
                        <Autocomplete
                                style={{width: "450px", fontSize: "18px"}}
                                id="destination"
                                options={destinations}
                                getOptionLabel={(option) => `${option.title} -> ${option.geolocation}, ${option.description}`}
                                renderInput={(params) => <TextField {...params} variant="outlined" label="Destination" />}
                                filterOptions={(x) => x}
                                onInputChange={handleInputChange}
                                onChange={(event, value) => {
                                    if (value) {
                                        console.log(value);
                                        setDestination({ ...destination, title: value.title, image: value.image, geolocation: value.geolocation, description: value.description });
                                    }
                                }}
                        />
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
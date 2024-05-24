INSERT INTO doc_search_doctor (
	first_name,
	last_name,
	specialization,
	floor_location,
	room_location
)
VALUES ('Hubertus', 'Harrington', 'GP', 'F1', 'R1'),
		('Susan', 'Sinister', 'IM', 'F1', 'R2'),
		('Michael', 'Monroe', 'ORTH', 'F1', 'R3'),
		('Maria', 'Meyer', 'CARD', 'F1', 'R4'),
		('John', 'Jonson', 'DENT', 'F2', 'R1'),
		('Veronica', 'Velucci', 'GYN', 'F2', 'R2'),
		('Allan', 'Alcot', 'PUL', 'F2', 'R3'),
		('Debra', 'Denver', 'GP', 'F2', 'R4'),
		('Josh', 'Jameson', 'DENT', 'F3', 'R1'),
		('Hillary', 'Harrington', 'IM', 'F3', 'R2')
ON CONFLICT DO NOTHING;
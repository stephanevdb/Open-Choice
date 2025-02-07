# Open-Choice

Open-Choice is a simple poll generator web application built with Flask. Users can create polls with custom questions and options, vote on options, and view poll results. Each device can only vote once per option to ensure fair voting.

## Features

- Create polls with custom questions and expiration dates.
- Add options to polls.
- Vote on poll options.
- View poll results.
- Restrict voting to once per device using cookies.

## Installation

### Prerequisites

- Python 3.12
- Docker (optional, for containerized deployment)

### Clone the Repository

```bash
git clone https://github.com/yourusername/Open-Choice.git
cd Open-Choice
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


## Running the Application

### Using Python

```bash
python app.py
```

### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t open-choice .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 open-choice
    ```

The application will be accessible at `http://localhost:5000`.

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Create a new poll by entering a question and optionally setting a custom ID and expiration date.
3. Add options to the poll.
4. Vote on the options.
5. View the poll results.



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

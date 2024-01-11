# load

![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/xtt28/load)

> [!WARNING]
> Unauthorized usage of stress-testing software on external servers may
> constitute a denial-of-service (DoS) attack. Please contact the owner of any
> server you wish to use this software on before proceeding. For liability
> information, reference the file [LICENSE](LICENSE).

## Description

load is a Python script that asynchronously tests the load-bearing capacity of
a provided server. Given the server, the amount of requests to make and the
amount of threads to use, the script will send GET requests with the above
parameters and record the response status and time. This information is then
aggregated and displayed to the user by means of standard output.

## Usage

### Install dependencies

```bash
# Install dependencies from requirements.txt
python3 -m pip install -r requirements.txt
```

### Commands

For an updated list of commands, run `python3 main.py -h`.

#### Options

| Option                | Required?       | Description                                |
| --------------------- | --------------- | ------------------------------------------ |
| -h, --help            | No              | Prints a list of command options.          |
| -u, --url URL         | Yes             | The URL of the website to test.            |
| -n, --num NUM         | No (default 10) | The amount of requests to make.            |
| -c, --threads THREADS | No (default 2)  | The amount of threads to use for the test. |

#### Example

```bash
# Pings http://localhost a total of 20 times with 5 threads
python3 main.py -u http://localhost -n 20 -c 5
```

## License

This application is licensed under the MIT License. For more details, please
reference the file [LICENSE](LICENSE).

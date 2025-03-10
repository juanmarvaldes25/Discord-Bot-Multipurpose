


!add <num1> <num2> ...

Adds a list of numbers.

Example: !add 5 10 15 → Result: 30

Session Management

!start

Starts a session and records the start time.

Example output: Session started at 14:30:15

!end

Ends the session and calculates the duration.

Example output: Session ended after 10 min 30.25 seconds

Transport Commands

!bus <stop_id>

Fetches the next bus departure time for the given stop ID.

Example: !bus 12345 → Next bus at 14:45

Task Scheduling

The bot will periodically send reminders in the specified channel.

Logging & Debugging

Uses Python’s logging module for structured logging.

Errors are logged with detailed messages to aid debugging.

Future Enhancements

Expand transport tracking to include trains and ferries.

Add interactive UI elements with Discord embeds.

Implement more database-backed features for persistent user settings.

License

This project is licensed under the MIT License.

Feel free to modify and expand the bot’s functionality!

TODO:
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
unit tests bus scraper
Postgre SQL via RENDER, for config data per user! may need an interface for discord -> bot -> handler -> processor into SQL -> retrieve from DB 
then it goes from DB -> processor, which calls the selenium methods -> databack to handler -> back to bot

only the PROCESSOR should call the functions from busreq and DB


openAI trANSALTION

more bus functionality




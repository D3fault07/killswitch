# Universal Killswitch Script

A simple Python script that acts as a remote killswitch. By checking a URL for specific content, you can control whether the script runs or exits.

## How It Works

The script fetches data from a specified URL (like a raw Pastebin link). If the content at the URL reads "on" the script stops. If it reads "off" the script continues to run as intended.

## Setup

1. **Create a Remote Killswitch**:
   - Use a service like [Pastebin](https://pastebin.com/) or GitHub to create a file containing "on" or "off".
   - Make sure the link is a raw URL so the script can access the plain text.

2. **Configure the Script**:
   - In the script, replace `%URL%` with your raw URL.

3. **Implement it into ur main program**:
   - Put the script at the topmost line so that it executes first before anything else does.
   - Nuitka is recommended for compilation of the sript since the killswitch could be bypassed if done by pyinstaller.
   - Even if compiled with Nuitka it can be bypassed but most basic user wont be able to do that.

4. **Run the Script**:
   - Execute the script. It will check the URL before proceeding:
     - If the content is "on": The killswitch is active, and the script exits.
     - If the content is "off": The script runs normally.

## Example Output

- **If killswitch is active ("on")**:
  ```
  Killswitch Active program will exit
  Exiting the program.
  ```

- **If killswitch is inactive ("off")**:
  ```
  killswitch is not active
  ```

## Notes
- Some firewall settings may block the scripts access to the URL.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



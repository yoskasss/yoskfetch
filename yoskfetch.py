from rich import print
import platform
import argparse
import os
import sys


def detect_execution_env():
    """
    Çalıştırılma ortamını algılar.
    """
    if getattr(sys, 'frozen', False):
        return "Executable (.exe)"  # Örneğin, PyInstaller ile oluşturulmuş
    elif os.getenv("PROMPT"):  # CMD ortamı
        return "Command Prompt (cmd)"
    elif os.getenv("POWERSHELL_DISTRIBUTION_CHANNEL"):  # PowerShell ortamı
        return "PowerShell"
    else:
        return "Unknown Environment"


def get_system_info(ascii_color="white"):
    """
    Sistem bilgilerini ve ASCII art'ı renkli bir şekilde yazdırır.
    """
    environment = detect_execution_env()
    device_name = platform.node()
    info = {
        "OS": platform.system(),
        "Kernel": platform.release(),
        "Name": device_name,
        "Theme": ascii_color,
        "Environment": environment,
    }

    ascii_art = """


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠴⠒⡶⠛⡉⠈⠉⠻⣌⠉⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⠇⠀⡸⠁⠀⠘⣆⠀⠀⠈⠳⣄⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡼⢱⠃⠀⠠⡇⠀⠀⡆⠘⡄⠀⠀⠀⠈⠳⡄⠀⠹⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡼⢣⠇⠀⠀⢀⣇⣀⣎⢹⣀⣹⣀⣀⣀⣀⣀⠘⡄⠀⢹⡀⠀⠀⠀⠀⠀
⠀⠀⢰⠃⣸⠒⠉⠉⠉⠉⠁⠘⠚⠀⠀⠀⠀⠀⠀⠀⢹⢻⡀⠀⢧⠀⠀⠀⠀⠀
⠀⠀⡜⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣇⠀⢸⠀⠀⠀⠀⠀
⠀⠀⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠸⠀⢰⡇⠀⠀⠀⠀
⠀⢸⡃⠸⠿⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⡇⠀⠀⠈⡇⠀⠀⠀⠀
⠀⢸⡇⠀⢻⠀⠀⠀⠘⠛⠀⠀⠉⠁⠀⠈⠟⠁⠀⠀⠀⡇⠀⡀⢠⡇⠀⠀⠀⠀
⠀⣼⢹⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡇⠈⡇⠀⠀⠀⠀
⠀⢹⣼⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡇⠐⡇⠀⠀⠀⠀
⠀⢸⣿⡄⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⠀⡇⠀⡇⠀⠀⠀⠀
⠀⠀⢿⣧⣿⣿⠤⢤⠤⠤⡶⢶⣤⣔⣶⣶⣶⣶⢲⢶⠲⡏⠀⡇⢠⣿⠀⠀⠀⠀
⠀⠀⠈⢻⣹⡎⡁⢸⠀⣆⣷⣼⣿⣿⣿⣿⠏⢹⣜⣼⢠⠃⠀⡇⠈⣻⡀⠀⠀⠀
⠀⠀⠀⠀⡿⡇⢸⡈⣇⣿⣿⡿⠛⠟⠛⠁⠀⠸⢿⡿⣼⣀⡀⠁⠘⢿⡇⠀⠀⠀
⠀⠀⠀⠀⣧⣡⣴⡟⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣼⣧⣿⣿⣿⣿⣶⣾⣿⣀⠀⠀
⠀⣠⣶⣿⣿⣟⣿⣿⣿⣿⣿⣿⣦⢖⣒⣒⡶⣴⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣷⡀
⢠⣿⣿⣿⣿⣿⣿⣿⡟⠳⣯⣻⣿⣿⣿⣿⣿⣿⢟⣵⠟⠉⣼⣿⣿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠙⠮⣿⣿⣿⣿⡿⠋⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠁
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⡀⠈⠻⡿⠋⢀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧
⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠈⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃


"""

    if platform.system() == "Windows":
        ascii_art = """Made By yoskAss
                                            ....                           
                           ....:::^^~^~~!!!!!!!~                           
          ....:::^^^~~~. .!!!!!!!!!!!!!!!!!!!!!~                           
  :~~~~!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ~!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ~!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ~!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ~!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ~!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ~!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^~~~~~~~~~~~~~~~~~~~~. .~~~~~~~~~~~~~~~~~~~~~^                           
   .............  .  ..    . ..................                            
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  ^!!!!!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
  :~~~~!!!!!!!!!!!!!!!!. .!!!!!!!!!!!!!!!!!!!!!~                           
          ....:::^^^^~~. .!!!!!!!!!!!!!!!!!!!!!~                           
                            ....^:^^~^~~!!!!!!!~                           
                                            ....  
"""

    # Bilgi ve ASCII art'ı hizalamak için gerekli işlemler
    info_lines = [f"[bold blue]{key}:[/bold blue] {value}" for key, value in info.items()]
    ascii_lines = ascii_art.strip().split("\n")

    max_lines = max(len(ascii_lines), len(info_lines))

    # Bilgi kısmını hizalama
    info_padding = (max_lines - len(info_lines)) // 2
    info_lines = [""] * info_padding + info_lines + [""] * (max_lines - len(info_lines) - info_padding)

    # ASCII art'ı hizalama
    ascii_lines += [""] * (max_lines - len(ascii_lines))

    # Yan yana hizalı ve renkli çıktı
    for art_line, info_line in zip(ascii_lines, info_lines):
        print(f"[{ascii_color}]{art_line:<50}[/{ascii_color}] {info_line}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASCII art ve sistem bilgilerini gösterir.")
    parser.add_argument(
        "-c",
        "--color",
        type=str,
        default="white",
        help="ASCII art için renk seçimi (örn: red, green, blue)"
    )
    args = parser.parse_args()

    try:
        # Kullanıcı tarafından belirtilen renk ile sistem bilgilerini göster
        get_system_info(ascii_color=args.color)
    except Exception as e:
        print(f"[bold red]Bir hata oluştu:[/bold red] {e}")

"""
This code uses the speedtest-cli library
and results in internet connection data.

-> Requirements:
    . pip install speedtest-cli
"""

import speedtest
import webbrowser

speed = speedtest.Speedtest()
speed.get_servers()
speed.get_best_server()
speed.download()
speed.upload()
speed.results.share()

results = speed.results.dict()
print(results)
webbrowser.open_new(results['share'])

cd /private/
sudo rm -rf tftpboot
mkdir /Users/silvan/tftpboot
sudo ln -s /Users/silvan/tftpboot tftpboot
sudo launchctl unload -F /System/Library/LaunchDaemons/tftp.plist
sudo launchctl load -F /System/Library/LaunchDaemons/tftp.plist


cd /Users/silvan/tftpboot


archive download-sw /force-reload /overwrite tftp://10.0.0.185/ap3g2-k9w7-tar.153-3.JPK2.tar
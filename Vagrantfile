Vagrant.configure("2") do |config|
  config.vm.box = "generic/debian9"

  config.vm.box_check_update = true

  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"

  config.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)", use_dhcp_assigned_default_route: true
  config.vm.synced_folder "./sniffer", "/sniffer"

  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
      # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    echo "alias python='python3'" >> /root/.bashrc
    echo "cd /sniffer" >> /root/.bashrc
    apt-get update
    # DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
  SHELL
end

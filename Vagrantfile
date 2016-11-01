$script = <<SCRIPT
sudo apt-get update

sudo apt-get -y install \
     build-essential \
     python3 \
     python3-dev \
     python3-pip

pip3 install --upgrade pip
SCRIPT

Vagrant.configure("2") do |default|
	default.vm.box = "ubuntu/trusty64"
	default.vm.hostname = "social"

	# shell provisioning
	default.vm.provision "shell", inline: $script

	default.vm.provider "virtualbox" do |vbox|
		vbox.name = "social"
		vbox.memory = 1024
	end
end

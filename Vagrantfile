VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "priver/wheezy-amd64"
    config.vm.network "forwarded_port", guest: 80, host: 8080
end

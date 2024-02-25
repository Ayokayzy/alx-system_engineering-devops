# Define SSH client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "\
# Puppet-generated SSH client configuration
Host myserver
    HostName hostname
    User username
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}

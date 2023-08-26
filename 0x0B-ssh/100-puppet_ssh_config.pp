# Configure_SSH to_use the_private key and_refuse password_authentication
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  ensure  => present,
  require => File['/etc/ssh/ssh_config'],
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  ensure  => present,
  require => File['/etc/ssh/ssh_config'],
}

# Increase_the_amount of_traffic an_nginx can_handle.

# Increase_the_ULIMIT of_the_defaul_file
exec { 'fix--for--nginx':
  # Modify_the_ULIMIT_value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specif0y_the_path for_sed_command
  path    => '/etc/usr/local/bin/:/bin/',
}

# Restart_Nginx
exec { 'nginx-restart':
  # Restart_Nginx_service
  command => '/etc/init.d/nginx restart',
  # Specify_the_path for_init.d scrpt
  path    => '/etc/init.d/',
}

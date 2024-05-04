#puppet manifest to config our servers

exec { 'apt-update':
  command     => 'apt-get update',
  refreshonly => true,
}

exec { 'apt-upgrade':
  command     => 'apt-get -y upgrade',
  refreshonly => true,
}

package { 'nginx':
  ensure => installed,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}


file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Hello from the test web page',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file_line { 'nginx_config':
  path    => '/etc/nginx/sites-available/default',
  line    => "    location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}",
  after   => 'location / {',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

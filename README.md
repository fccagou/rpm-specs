# rpm-specs

## Motivation

I have created this repo because xautolock is not present in epel and
I would like to create an automatic building workflow to:

* Create rpm for some software that are not packaged
* Rebuild all packages for security reasons

I want it as simple as git clone && cd && buildall


## Installation


  sudo yum install -i rpmdevtools rpm-build patch git
  git clone https://github.com/fccagou/rpm-specs ~/rpmbuild

## Build all specs

  cd ~/rpmbuild/SPECS
  for s in *.spec; do rpmbuild -ba $s; done

## TODO

As fedora mock, using Docker can be usefull to avoid installing all build
requires paquages on the host.

* Make a {cenos,rhel,fedora}[6,7,..] docker images with rpm-build tools
* Run rpmbuild from docker container for each os
* Run yum install into container an make test case
* Add sign
* Define workflow
* Integrate CI.
* Run buildall for each pull update using .githooks
* add git-templates

* ...


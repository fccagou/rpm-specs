Name:           xautolock
Version:        2.2
Release:        5%{?dist}
Summary:        Xautolock X11 screen

License:        GPL
URL:            http://ibiblio.org/pub/Linux/X11/screensavers
Source0:        http://ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
Patch1:         %{name}-%{version}-union-wait.patch

BuildRequires: patch
BuildRequires: imake
BuildRequires: gcc
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel

Requires:      libxss 

%description
Xautolock  monitors  console activity  under the X window system, and
fires  up  a  program  of your choice if  nothing  happens  during  a
user configurable  period of time.  You can use this to automatically
start up a screen locker in case you tend to forget to do so manually
before having a coffee break.

Xautolock  will  typically  be used to lock the screen but it  really
doesn't care what program you make it start. The only real assumption
made  by  xautolock  is that  a new countdown  starts  as soon as the
locker exits. 


%prep
%setup -q 
%patch1 -p1

%build
xmkmf
make


%install
rm -rf $RPM_BUILD_ROOT
%make_install
make DESTDIR=%{buildroot} install.man


%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Mar 20 2019 fccagou <fccagou@gmail.com>  2.2-6
- Initial rspec
- Patch from https://git.archlinux.org/svntogit/community.git/plain/xautolock/trunk/union-wait.patch


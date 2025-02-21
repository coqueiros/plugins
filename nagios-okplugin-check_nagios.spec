%define debug_package %{nil}

Summary:	A set of Nagios plugins to check the health of a nagios host
Name:		nagios-okplugin-check_nagios
Version:	1.2
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://opensource.is/trac/wiki/check_nagios
Source0:	http://opensource.ok.is/trac/browser/nagios-plugins/check_multipath/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Pall Sigurdsson <palli@opensource.is>


%description
Checks health of Nagios service

%prep
%setup -q
perl -pi -e "s|/usr/lib|%{_libdir}|g" nrpe.d/check_nagios.cfg

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 check_nagios_configuration %{buildroot}%{_libdir}/nagios/plugins/check_nagios_configuration
install -D -p -m 0755 check_nagios_ghostservices %{buildroot}%{_libdir}/nagios/plugins/check_nagios_ghostservices
install -D -p -m 0755 check_nagios_needs_reload %{buildroot}%{_libdir}/nagios/plugins/check_nagios_needs_reload
install -D -p -m 0755 check_nagios_plugin_existance %{buildroot}%{_libdir}/nagios/plugins/check_nagios_plugin_existance
install -D -p -m 0755 nrpe.d/check_nagios.cfg %{buildroot}/etc/nrpe.d/check_nagios.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc  LICENSE
%{_libdir}/nagios/plugins/*
/etc/nrpe.d/check_nagios.cfg

%changelog
* Wed May 22 2013 Tomas Edwardsson <tommi@tommi.org> 1.2-1
- Modified to parse on epoch rather that syslog date (tommi@tommi.org)
- Emit unknown if unable to open the logfile and detect location
  (tommi@tommi.org)
- Fix tmp file cleanup (palli@opensource.is)

* Thu Aug 23 2012 Pall Sigurdsson <palli@opensource.is> 1.1-1
- Version number bumped
- bugfix, check_nagios_needs_reload check for reload instead of reparse
  (palli@opensource.is)
- fixed missing tempfile cleanup (root@manage.tr.is)

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 0.0.8-1
- LICENSE file added (palli@opensource.is)

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 0.0.7-1
- 

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 0.0.6-1
- new package built with tito


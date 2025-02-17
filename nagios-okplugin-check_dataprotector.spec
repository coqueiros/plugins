%define debug_package %{nil}

Summary:	Nagios Plugins to monitor HP Dataprotector
Name:		nagios-okplugin-check_dataprotector
Version:	2
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://opensource.is/trac/wiki/check_dataprotector
Source0:	http://opensource.ok.is/trac/browser/nagios-plugins/check_dataprotector/releases/nagios-okplugin-check_dataprotector-%{version}.tar.gz
Requires:	OB2-DA,OB2-CC
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Pall Sigurdsson <palli@opensource.is>



%description
Nagios Plugins to monitor HP Dataprotector

%prep
%setup -q
perl -pi -e "s|/usr/lib/|%{_libdir}/|g" nrpe.d/check_dataprotector.cfg
perl -pi -e "s|/usr/lib64/|%{_libdir}/|g" nrpe.d/check_dataprotector.cfg

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 check_dp_backups %{buildroot}%{_libdir}/nagios/plugins/check_dp_backups
install -D -p -m 0755 check_dp_idb %{buildroot}%{_libdir}/nagios/plugins/check_dp_idb
install -D -p -m 0755 check_dp_mountrequest %{buildroot}%{_libdir}/nagios/plugins/check_dp_mountrequest
install -D -p -m 0755 check_dp_pool %{buildroot}%{_libdir}/nagios/plugins/check_dp_pool
install -D -p -m 0755 check_dp_services %{buildroot}%{_libdir}/nagios/plugins/check_dp_services
install -D -p -m 0755 check_dp_tablespace %{buildroot}%{_libdir}/nagios/plugins/check_dp_tablespace
install -D -p -m 0755 nrpe.d/check_dataprotector.cfg %{buildroot}/etc/nrpe.d/check_dataprotector.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{_libdir}/nagios/plugins/*
/etc/nrpe.d/check_dataprotector.cfg

%changelog
* Thu Feb 20 2014 Pall Sigurdsson <palli@opensource.is> 2-1
- removed warning threshold of 60 (palli@opensource.is)
- contrib removed from plugin path (palli@opensource.is)

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 1.0.1-1
- new package built with tito

* Mon Sep  15 2010  Pall Sigurdsson <palli@opensource.is> 0.1-1
- Initial packaging

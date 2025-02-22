%define debug_package %{nil}

%define plugin_name	check_rhcs
%define version		0.0.4


Summary:	A Nagios plugin to check Red Hat Cluster suite (rhel5 and rhel6)
Name:		nagios-okplugin-%{plugin_name}
Version:	1
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://opensource.is/trac/wiki/%{plugin_name}
Source0:	http://opensource.ok.is/trac/browser/nagios-plugins/%{plugin_name}/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Pall Sigurdsson <palli@opensource.is>


%description
%{summary}

%prep
%setup -q
perl -pi -e "s|/usr/lib64|%{_libdir}|g" nrpe.d/%{plugin_name}.cfg

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 check_rhcs %{buildroot}%{_libdir}/nagios/plugins/check_rhcs
install -D -p -m 0755 check_rhcs_cman_group.sh %{buildroot}%{_libdir}/nagios/plugins/check_rhcs_cman_group.sh
install -D -p -m 0755 check_rhcs_manualfencing.sh %{buildroot}%{_libdir}/nagios/plugins/check_rhcs_manualfencing.sh
install -D -p -m 0755 check_rhcs_fence %{buildroot}%{_libdir}/nagios/plugins/check_rhcs_fence

install -D -p -m 0755 nrpe.d/%{plugin_name}.cfg %{buildroot}/etc/nrpe.d/%{plugin_name}.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%doc README LICENSE
%{_libdir}/nagios/plugins/*
/etc/nrpe.d/%{plugin_name}.cfg

%changelog
* Thu Feb 20 2014 Pall Sigurdsson <palli@opensource.is> 1-1
- Updated rhcs nrpe config as well (tommi@tommi.org)
- Added check for suspended services -Z (tommi@tommi.org)
- Fix broken libdir on 64-bit platforms (palli@opensource.is)

* Thu May 24 2012 Pall Sigurdsson <palli@opensource.is> 0.0.4-1
- version bump of check_rhcs (palli@opensource.is)
- check_rhcs_fence added for rhel6 compatibility (palli@opensource.is)
- copy/paste error removed from spec file (palli@opensource.is)

* Thu May 24 2012 Pall Sigurdsson <palli@opensource.is>
- make sure plugin exits cleanly if unable to run clustat -fx command
  (palli@opensource.is)
- check_rhcs_fence added for rhel6 compatibility (palli@opensource.is)
- copy/paste error removed from spec file (palli@opensource.is)

* Wed Mar 14 2012 Pall Sigurdsson <palli@opensource.is>
- 

* Wed Mar 14 2012 Pall Sigurdsson <palli@opensource.is> 0.0.3-1
- new package built with tito

* Wed Mar 14 2012 Pall Sigurdsson <palli@opensource.is> 0.0.3-1
- new package built with tito

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 0.0.2-1
- new package built with tito

Name:              monitorix
Version:           3.1.0
Release:           1%{?dist}
Summary:           A free, open source, lightweight system monitoring tool

License:           GPLv2
URL:               http://www.monitorix.org

Source0:           http://www.monitorix.org/%{name}-%{version}.tar.gz
Source1:           monitorix.service
Source2:           monitorix.logrotate

Requires:          perl
Requires:          perl-CGI
Requires:          perl-Config-General
Requires:          perl-DBI
Requires:          perl-HTTP-Server-Simple
Requires:          perl-libwww-perl
Requires:          perl-MailTools
Requires:          perl-MIME-Lite
Requires:          perl-XML-Simple
Requires:          rrdtool
Requires:          rrdtool-perl
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Monitorix is a free, open source, lightweight system monitoring tool designed
to monitor as many services and system resources as possible. It has been
created to be used under production Linux/UNIX servers, but due to its
simplicity and small size may also be used on embedded devices as well. 

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 docs/monitorix.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/monitorix
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 docs/monitorix.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/monitorix
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 monitorix.conf %{buildroot}%{_sysconfdir}/monitorix.conf
mkdir -p %{buildroot}%{_bindir}
install -m 755 monitorix %{buildroot}%{_bindir}/monitorix
mkdir -p %{buildroot}%{_libdir}/monitorix
install -m 644 lib/*.pm %{buildroot}%{_libdir}/monitorix
mkdir -p %{buildroot}%{_datadir}/monitorix
install -m 644 logo_top.png %{buildroot}%{_datadir}/monitorix
install -m 644 logo_bot.png %{buildroot}%{_datadir}/monitorix
install -m 644 monitorixico.png %{buildroot}%{_datadir}/monitorix
mkdir -p %{buildroot}%{_datadir}/monitorix/imgs
mkdir -p %{buildroot}%{_datadir}/monitorix/cgi
install -m 755 monitorix.cgi %{buildroot}%{_datadir}/monitorix/cgi
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/reports
install -m 644 reports/*.html %{buildroot}%{_localstatedir}/lib/monitorix/reports
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/usage
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 man/man5/monitorix.conf.5 %{buildroot}%{_mandir}/man5
install -m 644 man/man8/monitorix.8 %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/monitorix.service

%post
%systemd_post {%SOURCE1}

%preun
%systemd_preun {%SOURCE1}

%postun
%systemd_postun_with_restart {%SOURCE1}

%files
%doc Changes COPYING README README.nginx docs/monitorix-alert.sh docs/monitorix-apache.conf docs/monitorix-lighttpd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/monitorix
%config(noreplace) %{_sysconfdir}/sysconfig/monitorix
%config(noreplace) %{_sysconfdir}/monitorix.conf
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/*.html
%{_mandir}/man5/monitorix.conf.5.gz
%{_mandir}/man8/monitorix.8.gz
%{_unitdir}/monitorix.service
%{_bindir}/monitorix
%{_libdir}/monitorix/*.pm
%{_datadir}/monitorix/logo_top.png
%{_datadir}/monitorix/logo_bot.png
%{_datadir}/monitorix/monitorixico.png
%{_datadir}/monitorix/cgi/monitorix.cgi
%attr(777,root,root) %{_datadir}/monitorix/imgs
%attr(755,root,root) %{_localstatedir}/lib/monitorix/usage

%changelog
* Mon Apr 1 2013 Christopher Meng <rpm@cicku.me>
- 3.1.0
- Initial Package

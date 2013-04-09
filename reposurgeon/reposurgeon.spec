Name:               reposurgeon
Version:            2.32
Release:            1%{?dist}
Summary:            SCM Repository Manipulation Tool
Source:             http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.gz
URL:                http://www.catb.org/~esr/reposurgeon/
License:            BSD

BuildArch:          noarch

BuildRequires:      make, xmlto, asciidoc, python

Requires:           python

%description
Reposurgeon enables risky operations that version-control systems don't want to
let you do, such as editing past comments and metadata and removing commits. It
works with any version control system that can export and import git
fast-import streams, including git, hg, and bzr.

%prep
%setup -q

%build
make

%install
install -p -D -m 755 reposurgeon "%{buildroot}%{_bindir}/%{name}"
install -p -D -m 644 reposurgeon.1 "%{buildroot}%{_mandir}/man1/%{name}.1"

%files
%doc TODO COPYING NEWS README AUTHORS
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1*

%changelog
* Sun Apr 07 2013 Christopher Meng <rpm@cicku.me> - 2.32-1
- Initial package.

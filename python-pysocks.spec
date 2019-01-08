%{?scl:          %scl_package        python-pysocks}
%{!?scl:         %global pkg_name    %{name}}

%{?scl:
%filter_from_provides s|/opt/rh/.*/root/usr/bin/python.*||g;s|python.*abi.*$||g
%filter_from_requires s|/opt/rh/.*/root/usr/bin/python.*||g;s|python.*abi.*$||g
%filter_setup
}

%global distname PySocks
%global sum     A Python SOCKS client module

Name:               %{?scl_prefix}python-pysocks
Version:            1.5.7
Release:            8.bs1%{?dist}
Summary:            %{sum}

License:            BSD
URL:                https://github.com/Anorov/PySocks
Source0:            https://github.com/Anorov/PySocks/archive/%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      %{?pythonscl:%{pythonscl}-}python-devel

Requires:    %{?pythonscl:%{pythonscl}-}python
%{?scl:Requires:%scl_runtime}

Provides: %{?scl_prefix}python3-pysocks = %{version}-%{release}

%description
A fork of SocksiPy with bug fixes and extra features.

Acts as a drop-in replacement to the socket module. Featuring:

- SOCKS proxy client for Python 2.6 - 3.x
- TCP and UDP both supported
- HTTP proxy client included but not supported or recommended (you should use
  urllib2's or requests' own HTTP proxy interface)
- urllib2 handler included.

%prep
%autosetup -n %{distname}-%{version}

%build
%{?scl:scl enable %{scl} %{?pythonscl} - << \EOF}
python setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} %{?pythonscl} - << \EOF}
python setup.py install -O1 --skip-build --root %{buildroot} --install-purelib %{python_sitelib}
%{?scl:EOF}

#%%check
## No tests included in the tarball...
## https://github.com/Anorov/PySocks/issues/37
#%%{__python2} setup.py test

%files 
%%doc README.md
%%license LICENSE
%{python_sitelib}/socks.py*
%{python_sitelib}/sockshandler.py*
%{python_sitelib}/__pycache__/
%{python_sitelib}/%{distname}-%{version}*


%changelog
* Fri Feb 23 2018 Marek Skalický <mskalick@redhat.com> - 1.5.7-8
- Add -runtime requirement

* Thu Feb 08 2018 Marek Skalický <mskalick@redhat.com> - 1.5.7-7
- Install into rh-mongodb36 prefix

* Wed Dec 20 2017 Marek Skalický <mskalick@redhat.com> - 1.5.7-6
- Spec file cleanup

* Wed Dec 20 2017 Marek Skalický <mskalick@redhat.com> - 1.5.7-5
- Import sclo-python35 package from CentOS and change it to RHSCL

* Thu Jul 27 2017 Jaroslaw Polok <jaroslaw.polok@cern.ch>
- SCLo build.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.5.7-3
- Rebuild for Python 3.6

* Mon Nov 28 2016 Tim Orling <ticotimo@gmail.com> - 1.5.7-2
- Ship python34-pysocks in EL6

* Sat Sep 17 2016 Kevin Fenzi <kevin@scrye.com> - 1.5.7-1
- Update to 1.5.7

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 1.5.6-6
- Ship python34-pysocks in EPEL7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-4
- Change our conflicts on python-SocksiPy to an obsoletes/provides.
  https://bugzilla.redhat.com/show_bug.cgi?id=1334407

* Mon May 09 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-3
- Fix typo in explicit conflicts.

* Tue May 03 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-2
- We don't actually need setuptools here.

* Mon May 02 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-1
- Initial package for Fedora

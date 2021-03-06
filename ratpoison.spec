%define xsessiondir %{_datadir}/xsessions

Name:           ratpoison
Version:        1.4.9
Release:        2%{?dist}
Summary:        Minimalistic window manager
Group:          Applications/Productivity
License:        GPLv2+
URL:            http://www.nongnu.org/ratpoison/
Source0:        http://savannah.nongnu.org/download/ratpoison/%{name}-%{version}.tar.xz
Source1:	%{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libXft-devel
BuildRequires: libX11-devel
BuildRequires: readline-devel
BuildRequires: libXt-devel
BuildRequires: libXinerama-devel
BuildRequires: libXtst-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: texinfo
BuildRequires: gcc
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires: xterm

%description
Ratpoison is a simple window manager that relies solely on keyboard input as
opposed to keyboard and mouse input.

%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS -DHAVE_GETLINE"
%configure --disable-dependency-tracking
make %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{xsessiondir}
install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{xsessiondir}/
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/allwindows.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/clickframe.pl
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/genrpbindings
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpshowall.sh
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/rpws
chmod 755 ${RPM_BUILD_ROOT}/%{_datadir}/ratpoison/split.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%defattr(-,root,root,-)
%{_bindir}/ratpoison
%{_bindir}/rpws
%doc %{_datadir}/doc/ratpoison/
%{_infodir}/ratpoison.info.gz
%{_mandir}/man1/ratpoison.1.gz
%{_datadir}/ratpoison/
%{_datadir}/xsessions/ratpoison.desktop
%{_datadir}/emacs/site-lisp/ratpoison.el

%changelog
* Sun Dec 26 2021 Stephen Hassard <steve@hassard.net> - 1.4.9-2
- Improve EL9 builds

* Thu Oct 22 2021 Stephen Hassard <steve@hassard.net> - 1.4.9-1
- Update to 1.4.9

* Sun Feb 22 2015 Stephen Hassard <steve@hassard.net> - 1.4.8-1
- Upgrade to 1.4.8

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.6-2
- Perl 5.18 rebuild

* Tue Jul 09 2013 Kevin Fenzi <kevin@scrye.com> 1.4.6-1
- Update to 1.4.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.5-1
- Update to 1.4.5

* Tue Jul 14 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.4-4
- Add libXi-devel to BuildRequires

* Tue Jun 16 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.4-3
- Rebuild again now that bug #505774 is fixed. 

* Fri Jun 12 2009 Ville Skytt?? <ville.skytta at iki.fi> - 1.4.4-2
- Build with $RPM_OPT_FLAGS.
- Disable autotools dependency tracking for cleaner build logs and possible
  slight build speedup.

* Thu May 14 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.4-1
- Update to 1.4.4
- Add libXft-devel to BuildRequires

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.1-2
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 John Berninger <john at ncphotography dot com> - 1.4.1-1
- rebuild for deps

* Fri Aug 31 2007 John Berninger <john at ncphotography dot com> - 1.4.1-0
- update to 1.4.1 - bz 269821

* Sun Sep 10 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-5
- Mass rebuild of FC/FE6

* Tue Apr 11 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-4
- BuildRequires fixes for FC-devel (FC-6)

* Sat Apr  8 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-3
- Permissions fixes

* Sat Apr  8 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-2
- install-info fixup
- BuildRequires fixup

* Fri Apr  7 2006 John Berninger <johnw at berningeronline dot net> - 1.4.0-1
- Bumped to 1.4.0-1 from 1.3.0-2
- Conditional BuildRequires for FC4-- versus FC5++
- Various fixes per bugzilla review

* Mon Mar 13 2006 John Berninger <johnw at berningeronline dot net> - 1.3.0-2
- Added ratpoison.desktop file

* Sun Feb 19 2006 John Berninger <johnw at berningeronline dot net> - 1.3.0-1
- Initial specfile build for FE(4)

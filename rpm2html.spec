Summary:	Translates rpm database into HTML and RDF info
Summary(pl):	Generuje informacje o bazie RPM formacie HTML
Name:		rpm2html 
Version:	1.7
Release:	1
Group:		Utilities/System
Group(pl):	Narzêdzia/System
License:	W3C Copyright (BSD like)
Source0:	ftp://rufus.w3.org/pub/rpm2html/%{name}-%{version}.tar.gz
URL:		http://rufus.w3.org/linux/rpm2html/
BuildRequires:	popt-devel
BuildRequires:	rpm-devel
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rpm2html tries to solve 2 big problems one face when grabbing a RPM
package from a mirror on the net and trying to install it:
   - it gives more information than just the filename before installing
     the package.
   - it tries to solve the dependancy problem by analyzing all the
     Provides and Requires of the set of RPMs. It shows the cross
     references by the way of hypertext links. Rpm2html can now dump the
     metadata associated to RPM packages into standard RDF files.

%description -l pl
Rpm2html próbuje rozwi±zaæ 2 wielkie problemy gdy chcesz ¶ci±gn±æ nowy
pakiet z sieci i próbujesz go zainstalowaæ:
   - daje wiêcej informacji ni¿ sama nazwa pakietu
   - próbuje rozwi±zaæ problem zale¿no¶ci poprzez analizê wszystkich
     Provides i Requires w grupie RPMów. Pokazuje zale¿no¶ci w formie
     hiper-po³±czeñ. Rpm2html potrafi teraz zrzuciæ metadane wystepuj±ce w
     pakietach RPM do plików standardu RDF.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES BUGS PRINCIPLES README \
	rpm2html-*config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rpm2html
%{_datadir}/rpm2html

%config %verify(not size mtime md5) %{_sysconfdir}/rpm2html.config
%{_mandir}/man1/*

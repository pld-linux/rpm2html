Summary:	Translates rpm database into HTML and RDF info
Summary(pl):	Generuje informacje o bazie RPM formacie HTML
Name:		rpm2html 
Version:	1.3
Release:	1
Group:		Utilities/System
Group(pl):	Narzêdzia/System
License:	W3C Copyright (BSD like)
Source0:	ftp://rufus.w3.org/pub/rpm2html/%{name}-%{version}.tar.gz
Source1:	msg-apache.pl
Source2:	msg-apache.en
URL:		http://rufus.w3.org/linux/rpm2html/
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rpm2html tries to solve 2 big problems one face when
grabbing a RPM package from a mirror on the net and trying to
install it:
   - it gives more information than just the filename before
     installing the package.
   - it tries to solve the dependancy problem by analyzing all
     the Provides and Requires of the set of RPMs. It shows the
     cross references by the way of hypertext links. 
Rpm2html can now dump the metadata associated to RPM packages into
standard RDF files.

%description -l pl
Rpm2html próbuje rozwi±zaæ 2 wielkie problemy gdy chcesz
¶ci±gn±æ nowy pakiet z sieci i próbujesz go zainstalowaæ:
   - daje wiêcej informacji ni¿ sama nazwa pakietu
   - próbuje rozwi±zaæ problem zale¿no¶ci poprzez analizê
     wszystkich Provides i Requires w grupie RPMów. Pokazuje
     zale¿no¶ci w formie hiper-po³±czeñ.
Rpm2html potrafi teraz zrzuciæ metadane wystepuj±ce w pakietach
RPM do plików standardu RDF.

%prep
%setup -q

%build
LFLAGS="-s"; export LFLAGS
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/rpm"; export CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_datadir}/rpm2html

install rpm2html $RPM_BUILD_ROOT%{_bindir}

install msg.fr $RPM_BUILD_ROOT%{_datadir}/rpm2html
install msg.es $RPM_BUILD_ROOT%{_datadir}/rpm2html
install msg.de $RPM_BUILD_ROOT%{_datadir}/rpm2html
install msg.pl $RPM_BUILD_ROOT%{_datadir}/rpm2html

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/rpm2html
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/rpm2html

install rpm2html.config $RPM_BUILD_ROOT%{_sysconfdir}
install rpm2html.1 $RPM_BUILD_ROOT%{_mandir}/man1/rpm2html.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	CHANGES BUGS PRINCIPLES README \
	rpm2html-cdrom.config rpm2html-en.config \
	rpm2html.config.mirrors rpm2html-fr.config \
	rpm2html.config.resources rpm2html-rdf.config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,BUGS,PRINCIPLES,README}.gz
%doc {rpm2html-cdrom.config,rpm2html-en.config}.gz
%doc {rpm2html.config.mirrors,rpm2html-fr.config}.gz
%doc {rpm2html.config.resources,rpm2html-rdf.config}.gz

%attr(755,root,root) %{_bindir}/rpm2html
%dir %{_datadir}/rpm2html
%{_datadir}/rpm2html/*

%config %verify(not size mtime md5) /etc/rpm2html.config
%{_mandir}/man1/*

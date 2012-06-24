Summary:	Translates rpm database into HTML and RDF info
Summary(es.UTF-8):   Genera HTML y información RDF a partir de un banco de datos rpm
Summary(pl.UTF-8):   Generuje informacje o bazie RPM formacie HTML
Summary(pt_BR.UTF-8):   Gera HTML e informação RDF a partir de um banco de dados RPM
Name:		rpm2html
Version:	1.8.2
Release:	1
License:	W3C Copyright (BSD like)
Group:		Applications/System
Source0:	ftp://rpmfind.net/pub/rpm2html/%{name}-%{version}.tar.gz
# Source0-md5:	99e2c0c43a7c9dab996ed15291dbedc1
URL:		http://rpmfind.net/linux/rpm2html/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel
BuildRequires:	popt-devel
BuildRequires:	rpm-devel
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

%description -l es.UTF-8
Rpm2html intenta resolver uno de los grandes problemas que ocurren
cuando se desea obtener y instalar un paquete RPM:
- provee más información, además del nombre del archivo antes de
  instalar el paquete; intenta resolver las dependencias analizando todo
  que un
- conjunto de RPMs ofrece y requiere. Enseña las referencias cruzadas
  como links html.

Rpm2html puede ahora ofrecer los metadatos asociados a paquetes RPM en
formato RDF padrón.

%description -l pl.UTF-8
Rpm2html próbuje rozwiązać 2 wielkie problemy gdy chcesz ściągnąć nowy
pakiet z sieci i próbujesz go zainstalować:
- daje więcej informacji niż sama nazwa pakietu
- próbuje rozwiązać problem zależności poprzez analizę wszystkich
  Provides i Requires w grupie RPMów. Pokazuje zależności w formie
  hiper-połączeń. Rpm2html potrafi teraz zrzucić metadane występujące w
  pakietach RPM do plików standardu RDF.

%description -l pt_BR.UTF-8
Rpm2html tenta resolver dois grandes problemas que ocorrem quando se
deseja obter e instalar um pacote RPM:
- ele provê mais informações além do nome do arquivo antes de instalar
  o pacote;
- ele tenta resolver as dependências analisando tudo que um conjunto
  de RPMs fornece e requer. Ele mostra as referências cruzadas como
  links html. Rpm2html pode agora fornecer os metadados associados a
  pacotes RPM em formato RDF padrão.

%prep
%setup -q

%build
rm -f missing mkinstalldirs
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES BUGS PRINCIPLES README rpm2html-*config
%attr(755,root,root) %{_bindir}/rpm2html
%{_datadir}/rpm2html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rpm2html.config
%{_mandir}/man1/*

Summary:	Translates rpm database into HTML and RDF info
Summary(es):	Genera HTML y informaci�n RDF a partir de un banco de datos rpm
Summary(pl):	Generuje informacje o bazie RPM formacie HTML
Summary(pt_BR):	Gera HTML e informa��o RDF a partir de um banco de dados RPM
Name:		rpm2html
Version:	1.8.2
Release:	1
License:	W3C Copyright (BSD like)
Group:		Applications/System
Source0:	ftp://rufus.w3.org/pub/rpm2html/%{name}-%{version}.tar.gz
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

%description -l es
Rpm2html intenta resolver uno de los grandes problemas que ocurren
cuando se desea obtener y instalar un paquete RPM:
   - provee m�s informaci�n, adem�s del nombre del archivo antes de
     instalar el paquete; intenta resolver las dependencias analizando todo
     que un
   - conjunto de RPMs ofrece y requiere. Ense�a las referencias cruzadas
     como links html.

Rpm2html puede ahora ofrecer los metadatos asociados a paquetes RPM en
formato RDF padr�n.

%description -l pl
Rpm2html pr�buje rozwi�za� 2 wielkie problemy gdy chcesz �ci�gn�� nowy
pakiet z sieci i pr�bujesz go zainstalowa�:
   - daje wi�cej informacji ni� sama nazwa pakietu
   - pr�buje rozwi�za� problem zale�no�ci poprzez analiz� wszystkich
     Provides i Requires w grupie RPM�w. Pokazuje zale�no�ci w formie
     hiper-po��cze�. Rpm2html potrafi teraz zrzuci� metadane wystepuj�ce w
     pakietach RPM do plik�w standardu RDF.

%description -l pt_BR
Rpm2html tenta resolver dois grandes problemas que ocorrem quando se
deseja obter e instalar um pacote RPM:
   - ele prov� mais informa��es al�m do nome do arquivo antes de instalar
     o pacote;
   - ele tenta resolver as depend�ncias analisando tudo que um conjunto
     de RPMs fornece e requer. Ele mostra as refer�ncias cruzadas como
     links html. Rpm2html pode agora fornecer os metadados associados a
     pacotes RPM em formato RDF padr�o.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES BUGS PRINCIPLES README rpm2html-*config
%attr(755,root,root) %{_bindir}/rpm2html
%{_datadir}/rpm2html

%config %verify(not size mtime md5) %{_sysconfdir}/rpm2html.config
%{_mandir}/man1/*

Summary:	Small fast XML parser
Summary(pl.UTF-8):	Mały, szybki analizator XML-a
Name:		piccolo
Version:	1.04
Release:	0.1
License:	LGPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/piccolo/%{name}-%{version}-src.zip
# Source0-md5:	35448ca6895f716ec14ab11430fd9650
URL:		http://piccolo.sourceforge.net/
BuildRequires:	ant >= 0:1.6
BuildRequires:	ant-junit
BuildRequires:	java-gcj-compat-devel
BuildRequires:	jpackage-utils >= 0:1.5.32
BuildRequires:	junit
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Piccolo is a small, extremely fast XML parser for Java. It implements
the SAX 1, SAX 2.0.1, and JAXP 1.1 (SAX parsing only) interfaces as a
non-validating parser and attempts to detect all XML well-formedness
errors.

%description -l pl.UTF-8
Piccolo to mały, bardzo szybki analizator XML-a dla Javy. Implementuje
interfejsy SAX 1, SAX 2.0.1 i JAXP 1.1 (tylko w zakresie analizy SAX)
jako analizator nie kontrolujący poprawności oraz próbuje wykryć
wszystkie błędy dobrego formułowania XML.

%package javadoc
Summary:	Javadoc for Piccolo
Summary(pl.UTF-8):	Dokumentacja javadoc do Piccolo
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc documentation for Piccolo.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc do Piccolo.

%description javadoc -l fr.UTF-8
Javadoc pour Piccolo.

%prep
%setup -q

%build
export OPT_JAR_LIST="ant/ant-junit junit"
%ant clean
%ant -Dbuild.sysclasspath=first \
	-Dbuild.compiler=gcj \
	build javadoc

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a lib/Piccolo.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

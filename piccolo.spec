%include	/usr/lib/rpm/macros.java
Summary:	Small fast XML parser
Name:		piccolo
Version:	1.04
Release:	0.1
License:	LGPL
Group:		Applications/Text
URL:		http://piccolo.sourceforge.net/
Source0:	http://dl.sourceforge.net/piccolo/%{name}-%{version}-src.zip
# Source0-md5:	35448ca6895f716ec14ab11430fd9650
BuildRequires:	ant >= 0:1.6
BuildRequires:	ant-junit
BuildRequires:	jpackage-utils >= 0:1.5.32
BuildRequires:	junit
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Piccolo is a small, extremely fast XML parser for Java. It implements
the SAX 1, SAX 2.0.1, and JAXP 1.1 (SAX parsing only) interfaces as a
non-validating parser and attempts to detect all XML well-formedness
errors.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name} -

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -q
find -name '*.jar' | xargs rm -vf

%build
export OPT_JAR_LIST="ant/ant-junit junit"
%ant -Dbuild.sysclasspath=first \
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

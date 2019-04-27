#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oiio
Version  : 1.8.17
Release  : 10
URL      : https://github.com/OpenImageIO/oiio/archive/Release-1.8.17.tar.gz
Source0  : https://github.com/OpenImageIO/oiio/archive/Release-1.8.17.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: oiio-bin = %{version}-%{release}
Requires: oiio-data = %{version}-%{release}
Requires: oiio-lib = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}
BuildRequires : LibRaw-dev
BuildRequires : OpenColorIO-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : opencv-dev
BuildRequires : openexr-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(IlmBase)
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pugixml-dev
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
======================
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg?style=flat-square)](https://github.com/OpenImageIO/oiio/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/OpenImageIO/oiio.svg?branch=master)](https://travis-ci.org/OpenImageIO/oiio)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/a0l32ti7gcoergtf/branch/master?svg=true)](https://ci.appveyor.com/api/projects/status/a0l32ti7gcoergtf/branch/master)

%package bin
Summary: bin components for the oiio package.
Group: Binaries
Requires: oiio-data = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}

%description bin
bin components for the oiio package.


%package data
Summary: data components for the oiio package.
Group: Data

%description data
data components for the oiio package.


%package dev
Summary: dev components for the oiio package.
Group: Development
Requires: oiio-lib = %{version}-%{release}
Requires: oiio-bin = %{version}-%{release}
Requires: oiio-data = %{version}-%{release}
Provides: oiio-devel = %{version}-%{release}
Requires: oiio = %{version}-%{release}

%description dev
dev components for the oiio package.


%package doc
Summary: doc components for the oiio package.
Group: Documentation

%description doc
doc components for the oiio package.


%package lib
Summary: lib components for the oiio package.
Group: Libraries
Requires: oiio-data = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}

%description lib
lib components for the oiio package.


%package license
Summary: license components for the oiio package.
Group: Default

%description license
license components for the oiio package.


%prep
%setup -q -n oiio-Release-1.8.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556387127
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DSTOP_ON_WARNING=OFF \
-DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR \
-DINSTALL_DOCS:BOOL=ON \
-DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
-DCMAKE_INSTALL_MANDIR:PATH=%{_mandir}/man1 \
-DINSTALL_FONTS:BOOL=ON \
-DBUILDSTATIC:BOOL=OFF \
-DLINKSTATIC:BOOL=OFF \
-DUSE_EXTERNAL_PUGIXML:BOOL=ON \
-DUSE_FFMPEG:BOOL=OFF \
-DUSE_OPENSSL:BOOL=ON \
-DCMAKE_SKIP_RPATH:BOOL=ON \
-DUSE_OPENCV:BOOL=ON \
-DUSE_PYTHON:BOOL=OFF \
-DCMAKE_DL_LIBS=dl \
-DOpenGL_GL_PREFERENCE=GLVND
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1556387127
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oiio
cp LICENSE %{buildroot}/usr/share/package-licenses/oiio/LICENSE
cp src/fonts/Droid_Sans/LICENSE.txt %{buildroot}/usr/share/package-licenses/oiio/src_fonts_Droid_Sans_LICENSE.txt
cp src/fonts/Droid_Sans_Mono/LICENSE.txt %{buildroot}/usr/share/package-licenses/oiio/src_fonts_Droid_Sans_Mono_LICENSE.txt
cp src/fonts/Droid_Serif/LICENSE.txt %{buildroot}/usr/share/package-licenses/oiio/src_fonts_Droid_Serif_LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iconvert
/usr/bin/idiff
/usr/bin/igrep
/usr/bin/iinfo
/usr/bin/iv
/usr/bin/maketx
/usr/bin/oiiotool

%files data
%defattr(-,root,root,-)
/usr/share/fonts/OpenImageIO/DroidSans-Bold.ttf
/usr/share/fonts/OpenImageIO/DroidSans.ttf
/usr/share/fonts/OpenImageIO/DroidSansMono.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-Bold.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-BoldItalic.ttf
/usr/share/fonts/OpenImageIO/DroidSerif-Italic.ttf
/usr/share/fonts/OpenImageIO/DroidSerif.ttf

%files dev
%defattr(-,root,root,-)
/usr/include/OpenImageIO/SHA1.h
/usr/include/OpenImageIO/argparse.h
/usr/include/OpenImageIO/array_view.h
/usr/include/OpenImageIO/atomic.h
/usr/include/OpenImageIO/benchmark.h
/usr/include/OpenImageIO/color.h
/usr/include/OpenImageIO/dassert.h
/usr/include/OpenImageIO/deepdata.h
/usr/include/OpenImageIO/errorhandler.h
/usr/include/OpenImageIO/export.h
/usr/include/OpenImageIO/filesystem.h
/usr/include/OpenImageIO/filter.h
/usr/include/OpenImageIO/fmath.h
/usr/include/OpenImageIO/fstream_mingw.h
/usr/include/OpenImageIO/function_view.h
/usr/include/OpenImageIO/hash.h
/usr/include/OpenImageIO/image_view.h
/usr/include/OpenImageIO/imagebuf.h
/usr/include/OpenImageIO/imagebufalgo.h
/usr/include/OpenImageIO/imagebufalgo_util.h
/usr/include/OpenImageIO/imagecache.h
/usr/include/OpenImageIO/imageio.h
/usr/include/OpenImageIO/missing_math.h
/usr/include/OpenImageIO/oiioversion.h
/usr/include/OpenImageIO/optparser.h
/usr/include/OpenImageIO/osdep.h
/usr/include/OpenImageIO/parallel.h
/usr/include/OpenImageIO/paramlist.h
/usr/include/OpenImageIO/platform.h
/usr/include/OpenImageIO/plugin.h
/usr/include/OpenImageIO/refcnt.h
/usr/include/OpenImageIO/simd.h
/usr/include/OpenImageIO/span.h
/usr/include/OpenImageIO/strided_ptr.h
/usr/include/OpenImageIO/string_view.h
/usr/include/OpenImageIO/strutil.h
/usr/include/OpenImageIO/sysutil.h
/usr/include/OpenImageIO/texture.h
/usr/include/OpenImageIO/thread.h
/usr/include/OpenImageIO/timer.h
/usr/include/OpenImageIO/tinyformat.h
/usr/include/OpenImageIO/typedesc.h
/usr/include/OpenImageIO/unittest.h
/usr/include/OpenImageIO/unordered_map_concurrent.h
/usr/include/OpenImageIO/ustring.h
/usr/include/OpenImageIO/varyingref.h
/usr/include/OpenImageIO/version.h
/usr/lib64/libOpenImageIO.so
/usr/lib64/libOpenImageIO_Util.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/oiio/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libOpenImageIO.so.1.8
/usr/lib64/libOpenImageIO.so.1.8.17
/usr/lib64/libOpenImageIO_Util.so.1.8
/usr/lib64/libOpenImageIO_Util.so.1.8.17

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oiio/LICENSE
/usr/share/package-licenses/oiio/src_fonts_Droid_Sans_LICENSE.txt
/usr/share/package-licenses/oiio/src_fonts_Droid_Sans_Mono_LICENSE.txt
/usr/share/package-licenses/oiio/src_fonts_Droid_Serif_LICENSE.txt

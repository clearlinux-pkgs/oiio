#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: f032afc
#
Name     : oiio
Version  : 2.4.6.1
Release  : 50
URL      : https://github.com/OpenImageIO/oiio/archive/v2.4.6.1/oiio-2.4.6.1.tar.gz
Source0  : https://github.com/OpenImageIO/oiio/archive/v2.4.6.1/oiio-2.4.6.1.tar.gz
Summary  : OpenImageIO is a library for reading and writing images.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: oiio-bin = %{version}-%{release}
Requires: oiio-data = %{version}-%{release}
Requires: oiio-lib = %{version}-%{release}
Requires: oiio-license = %{version}-%{release}
BuildRequires : Imath-dev
BuildRequires : LibRaw-dev
BuildRequires : OpenColorIO-data
BuildRequires : OpenColorIO-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : fmt-dev
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : opencv-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pugixml-dev
BuildRequires : python3-dev
BuildRequires : robin-map-dev
BuildRequires : tbb-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
======================
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg?style=flat-square)](https://github.com/OpenImageIO/oiio/blob/master/LICENSE.md)
[![CI](https://github.com/OpenImageIO/oiio/actions/workflows/ci.yml/badge.svg)](https://github.com/OpenImageIO/oiio/actions/workflows/ci.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2694/badge)](https://bestpractices.coreinfrastructure.org/projects/2694)

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
%setup -q -n oiio-2.4.6.1
cd %{_builddir}/oiio-2.4.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697746763
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -Wno-dev \
-DBUILDSTATIC:BOOL=OFF \
-DBUILD_MISSING_FMT:BOOL=OFF \
-DCMAKE_DL_LIBS=dl \
-DCMAKE_INSTALL_DOCDIR:PATH=/usr/share/doc/oiio \
-DCMAKE_INSTALL_MANDIR:PATH=/usr/share/man/man1 \
-DCMAKE_SKIP_RPATH:BOOL=ON \
-DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR \
-DINSTALL_DOCS:BOOL=ON \
-DINSTALL_FONTS:BOOL=ON \
-DLINKSTATIC:BOOL=OFF \
-DOpenGL_GL_PREFERENCE=GLVND \
-DSTOP_ON_WARNING=OFF \
-DUSE_EXTERNAL_PUGIXML:BOOL=ON \
-DUSE_FFMPEG:BOOL=OFF \
-DUSE_OPENCV:BOOL=ON \
-DUSE_OPENSSL:BOOL=ON \
-DUSE_PYTHON:BOOL=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -Wno-dev \
-DBUILDSTATIC:BOOL=OFF \
-DBUILD_MISSING_FMT:BOOL=OFF \
-DCMAKE_DL_LIBS=dl \
-DCMAKE_INSTALL_DOCDIR:PATH=/usr/share/doc/oiio \
-DCMAKE_INSTALL_MANDIR:PATH=/usr/share/man/man1 \
-DCMAKE_SKIP_RPATH:BOOL=ON \
-DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR \
-DINSTALL_DOCS:BOOL=ON \
-DINSTALL_FONTS:BOOL=ON \
-DLINKSTATIC:BOOL=OFF \
-DOpenGL_GL_PREFERENCE=GLVND \
-DSTOP_ON_WARNING=OFF \
-DUSE_EXTERNAL_PUGIXML:BOOL=ON \
-DUSE_FFMPEG:BOOL=OFF \
-DUSE_OPENCV:BOOL=ON \
-DUSE_OPENSSL:BOOL=ON \
-DUSE_PYTHON:BOOL=OFF
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697746763
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oiio
cp %{_builddir}/oiio-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/oiio/ed2d01d8d15c106c1a00da431acc00882046f3e7 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/iconvert
/V3/usr/bin/idiff
/V3/usr/bin/igrep
/V3/usr/bin/iinfo
/V3/usr/bin/iv
/V3/usr/bin/maketx
/V3/usr/bin/oiiotool
/V3/usr/bin/testtex
/usr/bin/iconvert
/usr/bin/idiff
/usr/bin/igrep
/usr/bin/iinfo
/usr/bin/iv
/usr/bin/maketx
/usr/bin/oiiotool
/usr/bin/testtex

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
/usr/include/OpenImageIO/Imath.h
/usr/include/OpenImageIO/argparse.h
/usr/include/OpenImageIO/array_view.h
/usr/include/OpenImageIO/atomic.h
/usr/include/OpenImageIO/attrdelegate.h
/usr/include/OpenImageIO/benchmark.h
/usr/include/OpenImageIO/color.h
/usr/include/OpenImageIO/dassert.h
/usr/include/OpenImageIO/deepdata.h
/usr/include/OpenImageIO/detail/farmhash.h
/usr/include/OpenImageIO/detail/fmt.h
/usr/include/OpenImageIO/detail/fmt/core.h
/usr/include/OpenImageIO/detail/fmt/format-inl.h
/usr/include/OpenImageIO/detail/fmt/format.h
/usr/include/OpenImageIO/detail/fmt/ostream.h
/usr/include/OpenImageIO/detail/fmt/printf.h
/usr/include/OpenImageIO/errorhandler.h
/usr/include/OpenImageIO/export.h
/usr/include/OpenImageIO/filesystem.h
/usr/include/OpenImageIO/filter.h
/usr/include/OpenImageIO/fmath.h
/usr/include/OpenImageIO/fstream_mingw.h
/usr/include/OpenImageIO/function_view.h
/usr/include/OpenImageIO/half.h
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
/usr/include/OpenImageIO/parallel.h
/usr/include/OpenImageIO/paramlist.h
/usr/include/OpenImageIO/platform.h
/usr/include/OpenImageIO/plugin.h
/usr/include/OpenImageIO/refcnt.h
/usr/include/OpenImageIO/simd.h
/usr/include/OpenImageIO/span.h
/usr/include/OpenImageIO/strided_ptr.h
/usr/include/OpenImageIO/string_view.h
/usr/include/OpenImageIO/strongparam.h
/usr/include/OpenImageIO/strutil.h
/usr/include/OpenImageIO/sysutil.h
/usr/include/OpenImageIO/texture.h
/usr/include/OpenImageIO/thread.h
/usr/include/OpenImageIO/tiffutils.h
/usr/include/OpenImageIO/timer.h
/usr/include/OpenImageIO/type_traits.h
/usr/include/OpenImageIO/typedesc.h
/usr/include/OpenImageIO/unittest.h
/usr/include/OpenImageIO/unordered_map_concurrent.h
/usr/include/OpenImageIO/ustring.h
/usr/include/OpenImageIO/varyingref.h
/usr/include/OpenImageIO/vecparam.h
/usr/include/OpenImageIO/version.h
/usr/lib64/cmake/OpenImageIO/OpenImageIOConfig.cmake
/usr/lib64/cmake/OpenImageIO/OpenImageIOConfigVersion.cmake
/usr/lib64/cmake/OpenImageIO/OpenImageIOTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OpenImageIO/OpenImageIOTargets.cmake
/usr/lib64/libOpenImageIO.so
/usr/lib64/libOpenImageIO_Util.so
/usr/lib64/pkgconfig/OpenImageIO.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/oiio/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libOpenImageIO.so.2.4.6
/V3/usr/lib64/libOpenImageIO_Util.so.2.4.6
/usr/lib64/libOpenImageIO.so.2.4
/usr/lib64/libOpenImageIO.so.2.4.6
/usr/lib64/libOpenImageIO_Util.so.2.4
/usr/lib64/libOpenImageIO_Util.so.2.4.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oiio/ed2d01d8d15c106c1a00da431acc00882046f3e7

// Filename: pgSliderBarNotify.h
// Created by:  drose (18Aug05)
//
////////////////////////////////////////////////////////////////////
//
// PANDA 3D SOFTWARE
// Copyright (c) 2001 - 2004, Disney Enterprises, Inc.  All rights reserved
//
// All use of this software is subject to the terms of the Panda 3d
// Software license.  You should have received a copy of this license
// along with this source code; you will also find a current copy of
// the license at http://etc.cmu.edu/panda3d/docs/license/ .
//
// To contact the maintainers of this program write to
// panda3d-general@lists.sourceforge.net .
//
////////////////////////////////////////////////////////////////////

#ifndef PGSLIDERBARNOTIFY_H
#define PGSLIDERBARNOTIFY_H

#include "pandabase.h"
#include "pgItemNotify.h"

class PGSliderBar;

////////////////////////////////////////////////////////////////////
//       Class : PGSliderBarNotify
// Description : Objects that inherit from this class can receive
//               notify messages when a slider bar moves or otherwise
//               is reconfigured.
////////////////////////////////////////////////////////////////////
class EXPCL_PANDA PGSliderBarNotify : public PGItemNotify {
public:
  INLINE PGSliderBarNotify();

protected:
  virtual void slider_bar_adjust(PGSliderBar *slider_bar);
  virtual void slider_bar_set_range(PGSliderBar *slider_bar);

  friend class PGSliderBar;
};

#include "pgSliderBarNotify.I"

#endif

#!/usr/bin/env python3
"""
Defaults and definitions for global settings.
"""
import functools

from matplotlib import rcParamsDefault as _rc_matplotlib_default

from . import validate

# Initial synced properties
# NOTE: Important that linewidth is less than matplotlib default of 0.8. In general
# want the axes lines to look about as thick as text.
# NOTE: Important that default values are equivalent to the *validated* values
# used in the RcParams dictionaries. Otherwise _user_settings() detects changes.
# NOTE: We could just leave some settings empty and leave it up to Configurator
# to sync them when proplot is imported... but we also sync them here so that we
# can simply compare any Configurator state to these dictionaries and use save()
# to only save the settings changed by the user.
BLACK = 'black'
CYCLE = 'colorblind'
CMAPCYC = 'twilight'
CMAPDIV = 'BuRd'
CMAPSEQ = 'Fire'
CMAPCAT = 'colorblind10'
DIVERGING = 'div'
FRAMEALPHA = 0.8  # legend and colorbar
FONTNAME = 'sans-serif'
FONTSIZE = 9.0
GRIDALPHA = 0.1
GRIDBELOW = 'line'
GRIDPAD = 3.0
GRIDRATIO = 0.5  # differentiated from major by half size reduction
GRIDSTYLE = '-'
LABELPAD = 4.0  # default is 4.0, previously was 3.0
LARGESIZE = 'med-large'
LINEWIDTH = 0.6
MARGIN = 0.05
MATHTEXT = False
SMALLSIZE = 'medium'
TICKDIR = 'out'
TICKLEN = 4.0
TICKLENRATIO = 0.5  # very noticeable length reduction
TICKMINOR = True
TICKPAD = 2.0
TICKWIDTHRATIO = 0.8  # very slight width reduction
TITLEPAD = 5.0  # default is 6.0, previously was 3.0
WHITE = 'white'
ZLINES = 2  # default zorder for lines
ZPATCHES = 1

# TeX Gyre fonts used in proplot
# NOTE: This preserves the matplotlib font priority lists after the tex gyre fonts but
# unlike matplotlib they are alphabetized. Proplot guarantees first fonts in the list
# are present so really the only purpose of the remaining entries is to give users ideas
# for other fonts to try. Plus the order used in matplotlib seemed pretty arbitrary.
FONTS_CURSIVE = [
    'TeX Gyre Chorus',  # Chancery lookalike
    'Apple Chancery',
    'Felipa',
    'Sand',
    'Script MT',
    'Textile',
    'Zapf Chancery',
    'cursive',
]
FONTS_FANTASY = [
    'TeX Gyre Adventor',  # Avant Garde lookalike
    'Avant Garde',
    'Charcoal',
    'Chicago',
    'Comic Sans MS',
    'Futura',
    'Humor Sans',
    'Impact',
    'Optima',
    'Western',
    'xkcd',
    'fantasy',
]
FONTS_MONOSPACE = [
    'TeX Gyre Cursor',  # Courier lookalike
    'DejaVu Sans Mono',
    'Bitstream Vera Sans Mono',
    'Computer Modern Typewriter',
    'Andale Mono',
    'Courier New',
    'Courier',
    'Fixed',
    'Nimbus Mono L',
    'Terminal',
    'monospace',
]
FONTS_SANSSERIF = [
    'TeX Gyre Heros',  # Helvetica lookalike
    'DejaVu Sans',
    'Bitstream Vera Sans',
    'Computer Modern Sans Serif',
    'Arial',
    'Avenir',
    'Fira Math',
    'Fira Sans',
    'Frutiger',
    'Geneva',
    'Gill Sans',
    'Helvetica',
    'Lucid',
    'Lucida Grande',
    'Myriad Pro',
    'Noto Sans',
    'Roboto',
    'Source Sans Pro',
    'Tahoma',
    'Trebuchet MS',
    'Ubuntu',
    'Univers',
    'Verdana',
    'sans-serif',
]
FONTS_SERIF = [
    'TeX Gyre Schola',  # Century lookalike
    'TeX Gyre Bonum',  # Bookman lookalike
    'TeX Gyre Termes',  # Times New Roman lookalike
    'TeX Gyre Pagella',  # Palatino lookalike
    'DejaVu Serif',
    'Bitstream Vera Serif',
    'Computer Modern Roman',
    'Bookman',
    'Century Schoolbook L',
    'Charter',
    'ITC Bookman',
    'New Century Schoolbook',
    'Nimbus Roman No9 L',
    'Noto Serif',
    'Palatino',
    'Source Serif Pro',
    'Times New Roman',
    'Times',
    'Utopia',
    'serif',
]


# Proplot overrides of matplotlib default style
# WARNING: Critical to include every parameter here that can be changed by a
# "meta" setting so that _get_default_param returns the value imposed by *proplot*
# and so that "changed" settings detected by Configurator.save are correct.
_rc_matplotlib_override = {
    'axes.axisbelow': GRIDBELOW,
    'axes.formatter.use_mathtext': MATHTEXT,
    'axes.grid': True,  # lightweight default grid
    'axes.grid.which': 'major',  # major ticks only
    'axes.edgecolor': BLACK,
    'axes.labelcolor': BLACK,
    'axes.labelpad': LABELPAD,  # more compact
    'axes.labelsize': SMALLSIZE,
    'axes.labelweight': 'normal',
    'axes.linewidth': LINEWIDTH,
    'axes.titlepad': TITLEPAD,  # more compact
    'axes.titlesize': LARGESIZE,
    'axes.titleweight': 'normal',
    'axes.xmargin': MARGIN,
    'axes.ymargin': MARGIN,
    'errorbar.capsize': 3.0,
    'figure.autolayout': False,
    'figure.figsize': (4.0, 4.0),  # interactive backends
    'figure.dpi': 100,
    'figure.facecolor': '#f4f4f4',  # similar to MATLAB interface
    'figure.titlesize': LARGESIZE,  # differentiate from axes titles
    'figure.titleweight': 'bold',  # differentiate from axes titles
    'font.serif': FONTS_SERIF,
    'font.sans-serif': FONTS_SANSSERIF,
    'font.cursive': FONTS_CURSIVE,
    'font.fantasy': FONTS_FANTASY,
    'font.monospace': FONTS_MONOSPACE,
    'font.family': FONTNAME,
    'font.size': FONTSIZE,
    'grid.alpha': GRIDALPHA,  # lightweight unobtrusive gridlines
    'grid.color': BLACK,  # lightweight unobtrusive gridlines
    'grid.linestyle': GRIDSTYLE,
    'grid.linewidth': LINEWIDTH,
    'hatch.color': BLACK,
    'hatch.linewidth': LINEWIDTH,
    'image.cmap': CMAPSEQ,
    'lines.linestyle': '-',
    'lines.linewidth': 1.5,
    'lines.markersize': 6.0,
    'legend.borderaxespad': 0,  # i.e. flush against edge
    'legend.borderpad': 0.5,  # a bit more roomy
    'legend.columnspacing': 1.5,  # a bit more compact (see handletextpad)
    'legend.edgecolor': BLACK,
    'legend.facecolor': WHITE,
    'legend.fancybox': False,  # i.e. BboxStyle 'square' not 'round'
    'legend.fontsize': SMALLSIZE,
    'legend.framealpha': FRAMEALPHA,
    'legend.handleheight': 1.0,  # default is 0.7
    'legend.handlelength': 2.0,  # default is 2.0
    'legend.handletextpad': 0.5,  # a bit more compact (see columnspacing)
    'mathtext.default': 'it',
    'mathtext.fontset': 'custom',
    'mathtext.bf': 'regular:bold',  # custom settings implemented above
    'mathtext.cal': 'cursive',
    'mathtext.it': 'regular:italic',
    'mathtext.rm': 'regular',
    'mathtext.sf': 'regular',
    'mathtext.tt': 'monospace',
    'patch.facecolor': 'C0',
    'patch.linewidth': LINEWIDTH,
    'savefig.bbox': None,  # do not use 'tight'
    'savefig.directory': '',  # use the working directory
    'savefig.dpi': 1000,  # use academic journal recommendation
    'savefig.facecolor': WHITE,  # use white instead of 'auto'
    'savefig.format': 'pdf',  # use vector graphics
    'savefig.transparent': False,
    'xtick.color': BLACK,
    'xtick.direction': TICKDIR,
    'xtick.labelsize': SMALLSIZE,
    'xtick.major.pad': TICKPAD,
    'xtick.major.size': TICKLEN,
    'xtick.major.width': LINEWIDTH,
    'xtick.minor.pad': TICKPAD,
    'xtick.minor.size': TICKLEN * TICKLENRATIO,
    'xtick.minor.width': LINEWIDTH * TICKWIDTHRATIO,
    'xtick.minor.visible': TICKMINOR,
    'ytick.color': BLACK,
    'ytick.direction': TICKDIR,
    'ytick.labelsize': SMALLSIZE,
    'ytick.major.pad': TICKPAD,
    'ytick.major.size': TICKLEN,
    'ytick.major.width': LINEWIDTH,
    'ytick.minor.pad': TICKPAD,
    'ytick.minor.size': TICKLEN * TICKLENRATIO,
    'ytick.minor.width': LINEWIDTH * TICKWIDTHRATIO,
    'ytick.minor.visible': TICKMINOR,
}

# Proplot pseudo-setting defaults, validators, and descriptions
# NOTE: Cannot have different a-b-c and title paddings because they are both controlled
# by matplotlib's _title_offset_trans transform and want to keep them aligned anyway.
_addendum_em = ' Interpreted by `~proplot.utils.units`. Numeric units are em-widths.'
_addendum_in = ' Interpreted by `~proplot.utils.units`. Numeric units are inches.'
_addendum_pt = ' Interpreted by `~proplot.utils.units`. Numeric units are points.'
_addendum_rotation = " Must be 'vertical', 'horizontal', or a float indicating degrees."
_addendum_font = (
    ' Must be a :ref:`relative font size <font_table>` or unit string '
    'interpreted by `~proplot.utils.units`. Numeric units are points.'
)
_rc_proplot_definition = {
    # Global style
    'style': (
        None,
        validate._validate_style,
        'The default `style name or stylesheet filename '
        '<https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html>`__. '  # noqa: E501
        'This can be a name listed in `matplotlib.style.available`, a name listed '
        'in the `~proplot.config.use_style` :ref:`table <style_table>`, or a valid '
        'filename with settings adhering to ``matplotlibrc`` syntax. Use ``None`` to '
        "revert to the initial style settings after importing proplot or ``'default'`` "
        'to revert to the default matplotlib settings without proplot overrides.'
    ),

    # A-b-c labels
    'abc': (
        False,
        validate._validate_abc,
        'If ``False`` then a-b-c labels are disabled. If ``True`` the default label '
        'style ``a`` is used. If string this indicates the style and must contain the '
        "character ``a`` or ``A``, for example ``'a.'`` or ``'(A)'``."
    ),
    'abc.border': (
        True,
        validate._validate_bool,
        'Whether to draw a white border around a-b-c labels '
        'when :rcraw:`abc.loc` is inside the axes.'
    ),
    'abc.borderwidth': (
        1.5,
        validate._validate_pt,
        'Width of the white border around a-b-c labels.'
    ),
    'abc.bbox': (
        False,
        validate._validate_bool,
        'Whether to draw semi-transparent bounding boxes around a-b-c labels '
        'when :rcraw:`abc.loc` is inside the axes.'
    ),
    'abc.bboxcolor': (
        WHITE,
        validate._validate_color,
        'a-b-c label bounding box color.'
    ),
    'abc.bboxstyle': (
        'square',
        validate._validate_boxstyle,
        'a-b-c label bounding box style.'
    ),
    'abc.bboxalpha': (
        0.5,
        validate._validate_float,
        'a-b-c label bounding box opacity.'
    ),
    'abc.bboxpad': (
        None,
        validate._validate_or_none(validate._validate_pt),
        'Padding for the a-b-c label bounding box. By default this is scaled '
        'to make the box flush against the subplot edge.' + _addendum_pt
    ),
    'abc.color': (
        BLACK,
        validate._validate_color,
        'a-b-c label color.'
    ),
    'abc.loc': (
        'left',  # left side above the axes
        functools.partial(validate._validate_loc, mode='text'),
        'a-b-c label position. '
        'For options see the :ref:`location table <title_table>`.'
    ),
    'abc.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'a-b-c label font size.' + _addendum_font
    ),
    'abc.titlepad': (
        LABELPAD,
        validate._validate_pt,
        'Padding separating the title and a-b-c label when in the same location.'
        + _addendum_pt
    ),
    'abc.weight': (
        'bold',
        validate._validate_fontweight,
        'a-b-c label font weight.'
    ),

    # Autoformatting
    'autoformat': (
        True,
        validate._validate_bool,
        'Whether to automatically apply labels from `pandas.Series`, '
        '`pandas.DataFrame`, and `xarray.DataArray` objects passed to '
        'plotting functions. See also :rcraw:`unitformat`.'
    ),

    # Axes additions
    'axes.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity of the background axes patch.'
    ),
    'axes.inbounds': (
        True,
        validate._validate_bool,
        'Whether to exclude out-of-bounds data when determining the default *y* (*x*) '
        'axis limits and the *x* (*y*) axis limits have been locked.'
    ),
    'axes.margin': (
        MARGIN,
        validate._validate_float,
        'The fractional *x* and *y* axis margins when limits are unset.'
    ),

    # Country borders
    'borders': (
        False,
        validate._validate_bool,
        'Toggles country border lines on and off.'
    ),
    'borders.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for country border lines.',
    ),
    'borders.color': (
        BLACK,
        validate._validate_color,
        'Line color for country border lines.'
    ),
    'borders.linewidth': (
        LINEWIDTH,
        validate._validate_pt,
        'Line width for country border lines.'
    ),
    'borders.zorder': (
        ZLINES,
        validate._validate_float,
        'Z-order for country border lines.'
    ),

    # Bottom subplot labels
    'bottomlabel.color': (
        BLACK,
        validate._validate_color,
        'Font color for column labels on the bottom of the figure.'
    ),
    'bottomlabel.pad': (
        TITLEPAD,
        validate._validate_pt,
        'Padding between axes content and column labels on the bottom of the figure.'
        + _addendum_pt
    ),
    'bottomlabel.rotation': (
        'horizontal',
        validate._validate_rotation,
        'Rotation for column labels at the bottom of the figure.' + _addendum_rotation
    ),
    'bottomlabel.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'Font size for column labels on the bottom of the figure.' + _addendum_font
    ),
    'bottomlabel.weight': (
        'bold',
        validate._validate_fontweight,
        'Font weight for column labels on the bottom of the figure.'
    ),

    # Coastlines
    'coast': (
        False,
        validate._validate_bool,
        'Toggles coastline lines on and off.'
    ),
    'coast.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for coast lines',
    ),
    'coast.color': (
        BLACK,
        validate._validate_color,
        'Line color for coast lines.'
    ),
    'coast.linewidth': (
        LINEWIDTH,
        validate._validate_pt,
        'Line width for coast lines.'
    ),
    'coast.zorder': (
        ZLINES,
        validate._validate_float,
        'Z-order for coast lines.'
    ),

    # Colorbars
    'colorbar.edgecolor': (
        BLACK,
        validate._validate_color,
        'Color for the inset colorbar frame edge.'
    ),
    'colorbar.extend': (
        1.3,
        validate._validate_em,
        'Length of rectangular or triangular "extensions" for panel colorbars.'
        + _addendum_em
    ),
    'colorbar.fancybox': (
        False,
        validate._validate_bool,
        'Whether to use a "fancy" round bounding box for inset colorbar frames.'
    ),
    'colorbar.framealpha': (
        FRAMEALPHA,
        validate._validate_float,
        'Opacity for inset colorbar frames.'
    ),
    'colorbar.facecolor': (
        WHITE,
        validate._validate_color,
        'Color for the inset colorbar frame.'
    ),
    'colorbar.frameon': (
        True,
        validate._validate_bool,
        'Whether to draw a frame behind inset colorbars.'
    ),
    'colorbar.grid': (
        False,
        validate._validate_bool,
        'Whether to draw borders between each level of the colorbar.'
    ),
    'colorbar.insetextend': (
        0.9,
        validate._validate_em,
        'Length of rectangular or triangular "extensions" for inset colorbars.'
        + _addendum_em
    ),
    'colorbar.insetlength': (
        8,
        validate._validate_em,
        'Length of inset colorbars.' + _addendum_em
    ),
    'colorbar.insetpad': (
        0.7,
        validate._validate_em,
        'Padding between axes edge and inset colorbars.' + _addendum_em
    ),
    'colorbar.insetwidth': (
        1.2,
        validate._validate_em,
        'Width of inset colorbars.' + _addendum_em
    ),
    'colorbar.length': (
        1,
        validate._validate_em,
        'Length of outer colorbars.'
    ),
    'colorbar.loc': (
        'right',
        functools.partial(validate._validate_loc, mode='colorbar'),
        'Inset colorbar location. '
        'For options see the :ref:`location table <colorbar_table>`.'
    ),
    'colorbar.width': (
        0.2,
        validate._validate_in,
        'Width of outer colorbars.' + _addendum_in
    ),
    'colorbar.rasterized': (
        False,
        validate._validate_bool,
        'Whether to use rasterization for colorbar solids.'
    ),
    'colorbar.shadow': (
        False,
        validate._validate_bool,
        'Whether to add a shadow underneath inset colorbar frames.'
    ),

    # Color cycle additions
    'cycle': (
        CYCLE,
        validate._validate_cmap('discrete'),
        'Name of the color cycle assigned to :rcraw:`axes.prop_cycle`.'
    ),

    # Colormap additions
    'cmap': (
        CMAPSEQ,
        validate._validate_cmap('continuous'),
        'Alias for :rcraw:`cmap.sequential` and :rcraw:`image.cmap`.'
    ),
    'cmap.autodiverging': (
        True,
        validate._validate_bool,
        'Whether to automatically apply a diverging colormap and '
        'normalizer based on the data.'
    ),
    'cmap.qualitative': (
        CMAPCAT,
        validate._validate_cmap('discrete'),
        'Default colormap for qualitative datasets.'
    ),
    'cmap.cyclic': (
        CMAPCYC,
        validate._validate_cmap('continuous'),
        'Default colormap for cyclic datasets.'
    ),
    'cmap.discrete': (
        None,
        validate._validate_or_none(validate._validate_bool),
        'If ``True``, `~proplot.colors.DiscreteNorm` is used for every colormap plot. '
        'If ``False``, it is never used. If ``None``, it is used for all plot types '
        'except `imshow`, `matshow`, `spy`, `hexbin`, and `hist2d`.'
    ),
    'cmap.diverging': (
        CMAPDIV,
        validate._validate_cmap('continuous'),
        'Default colormap for diverging datasets.'
    ),
    'cmap.inbounds': (
        True,
        validate._validate_bool,
        'If ``True`` and the *x* and *y* axis limits are fixed, only in-bounds data '
        'is considered when determining the default colormap `vmin` and `vmax`.'
    ),
    'cmap.levels': (
        11,
        validate._validate_int,
        'Default number of `~proplot.colors.DiscreteNorm` levels for plotting '
        'commands that use colormaps.'
    ),
    'cmap.listedthresh': (
        64,
        validate._validate_int,
        'Native `~matplotlib.colors.ListedColormap`\\ s with more colors than '
        'this are converted to `~proplot.colors.ContinuousColormap` rather than '
        '`~proplot.colors.DiscreteColormap`. This helps translate continuous '
        'colormaps from external projects.'
    ),
    'cmap.lut': (
        256,
        validate._validate_int,
        'Number of colors in the colormap lookup table. '
        'Alias for :rcraw:`image.lut`.'
    ),
    'cmap.robust': (
        False,
        validate._validate_bool,
        'If ``True``, the default colormap `vmin` and `vmax` are chosen using the '
        '2nd to 98th percentiles rather than the minimum and maximum.'
    ),
    'cmap.sequential': (
        CMAPSEQ,
        validate._validate_cmap('continuous'),
        'Default colormap for sequential datasets. Alias for :rcraw:`image.cmap`.'
    ),

    # Special setting
    'edgefix': (
        True,
        validate._validate_bool,
        'Whether to fix issues with "white lines" appearing between patches '
        'in saved vector graphics and with vector graphic backends. Applies '
        'to colorbar levels and bar, area, pcolor, and contour plots.'
    ),

    # Font settings
    'font.name': (
        FONTNAME,
        validate._validate_fontname,
        'Alias for :rcraw:`font.family`.'
    ),
    'font.small': (
        SMALLSIZE,
        validate._validate_fontsize,
        'Alias for :rcraw:`font.smallsize`.'
    ),
    'font.smallsize': (
        SMALLSIZE,
        validate._validate_fontsize,
        'Meta setting that changes the label-like sizes ``axes.labelsize``, '
        '``legend.fontsize``, ``tick.labelsize``, and ``grid.labelsize``. Default is '
        "``'medium'`` (equivalent to :rcraw:`font.size`)." + _addendum_font
    ),
    'font.large': (
        LARGESIZE,
        validate._validate_fontsize,
        'Alias for :rcraw:`font.largesize`.'
    ),
    'font.largesize': (
        LARGESIZE,
        validate._validate_fontsize,
        'Meta setting that changes the title-like sizes ``abc.size``, ``title.size``, '
        '``suptitle.size``, ``leftlabel.size``, ``rightlabel.size``, etc. Default is '
        "``'med-large'`` (i.e. 1.1 times :rcraw:`font.size`)." + _addendum_font
    ),

    # Formatter settings
    'formatter.timerotation': (
        'vertical',
        validate._validate_rotation,
        'Rotation for *x* axis datetime tick labels.' + _addendum_rotation
    ),
    'formatter.zerotrim': (
        True,
        validate._validate_bool,
        'Whether to trim trailing decimal zeros on tick labels.'
    ),
    'formatter.limits': (
        [-5, 6],  # must be list or else validated
        validate._validate['axes.formatter.limits'],
        'Alias for :rcraw:`axes.formatter.limits`.'
    ),
    'formatter.min_exponent': (
        0,
        validate._validate['axes.formatter.min_exponent'],
        'Alias for :rcraw:`axes.formatter.min_exponent`.'
    ),
    'formatter.offset_threshold': (
        4,
        validate._validate['axes.formatter.offset_threshold'],
        'Alias for :rcraw:`axes.formatter.offset_threshold`.'
    ),
    'formatter.use_locale': (
        False,
        validate._validate_bool,
        'Alias for :rcraw:`axes.formatter.use_locale`.'
    ),
    'formatter.use_mathtext': (
        MATHTEXT,
        validate._validate_bool,
        'Alias for :rcraw:`axes.formatter.use_mathtext`.'
    ),
    'formatter.use_offset': (
        True,
        validate._validate_bool,
        'Alias for :rcraw:`axes.formatter.useOffset`.'
    ),

    # Geographic axes settings
    'geo.backend': (
        'cartopy',
        validate._validate_belongs('cartopy', 'basemap'),
        'The backend used for `~proplot.axes.GeoAxes`. Must be '
        "either 'cartopy' or 'basemap'."
    ),
    'geo.extent': (
        'globe',
        validate._validate_belongs('globe', 'auto'),
        "If ``'globe'``, the extent of cartopy `~proplot.axes.GeoAxes` is always "
        "global. If ``'auto'``, the extent is automatically adjusted based on "
        "plotted content. Default is ``'globe'``."
    ),
    'geo.round': (
        True,
        validate._validate_bool,
        "If ``True`` (the default), polar `~proplot.axes.GeoAxes` like ``'npstere'`` "
        "and ``'spstere'`` are bounded with circles rather than squares."
    ),

    # Gridlines
    # NOTE: Here 'grid' and 'gridminor' or *not* aliases for native 'axes.grid' and
    # invented 'axes.gridminor' because native 'axes.grid' controls both major *and*
    # minor gridlines. Must handle it independently from these settings.
    'grid': (
        True,
        validate._validate_bool,
        'Toggle major gridlines on and off.'
    ),
    'grid.below': (
        GRIDBELOW,  # like axes.axisbelow
        validate._validate_belongs(False, 'line', True),
        'Alias for :rcraw:`axes.axisbelow`. If ``True``, draw gridlines below '
        "everything. If ``True``, draw them above everything. If ``'line'``, "
        'draw them above patches but below lines and markers.'
    ),
    'grid.checkoverlap': (
        True,
        validate._validate_bool,
        'Whether to have cartopy automatically check for and remove overlapping '
        '`~proplot.axes.GeoAxes` gridline labels.'
    ),
    'grid.dmslabels': (
        True,
        validate._validate_bool,
        'Whether to use degrees-minutes-seconds rather than decimals for '
        'cartopy `~proplot.axes.GeoAxes` gridlines.'
    ),
    'grid.geolabels': (
        True,
        validate._validate_bool,
        "Whether to include the ``'geo'`` spine in cartopy >= 0.20 when otherwise "
        'toggling left, right, bottom, or top `~proplot.axes.GeoAxes` gridline labels.'
    ),
    'grid.inlinelabels': (
        False,
        validate._validate_bool,
        'Whether to add inline labels for cartopy `~proplot.axes.GeoAxes` gridlines.'
    ),
    'grid.labels': (
        False,
        validate._validate_bool,
        'Whether to add outer labels for `~proplot.axes.GeoAxes` gridlines.'
    ),
    'grid.labelcolor': (
        BLACK,
        validate._validate_color,
        'Font color for `~proplot.axes.GeoAxes` gridline labels.'
    ),
    'grid.labelpad': (
        GRIDPAD,
        validate._validate_pt,
        'Padding between the map boundary and cartopy `~proplot.axes.GeoAxes` '
        'gridline labels.' + _addendum_pt
    ),
    'grid.labelsize': (
        SMALLSIZE,
        validate._validate_fontsize,
        'Font size for `~proplot.axes.GeoAxes` gridline labels.' + _addendum_font
    ),
    'grid.labelweight': (
        'normal',
        validate._validate_fontweight,
        'Font weight for `~proplot.axes.GeoAxes` gridline labels.'
    ),
    'grid.nsteps': (
        250,
        validate._validate_int,
        'Number of points used to draw cartopy `~proplot.axes.GeoAxes` gridlines.'
    ),
    'grid.pad': (
        GRIDPAD,
        validate._validate_pt,
        'Alias for :rcraw:`grid.labelpad`.'
    ),
    'grid.rotatelabels': (
        False,  # False limits projections where labels are available
        validate._validate_bool,
        'Whether to rotate cartopy `~proplot.axes.GeoAxes` gridline labels.'
    ),
    'grid.style': (
        '-',
        validate._validate_linestyle,
        'Major gridline style. Alias for :rcraw:`grid.linestyle`.'
    ),
    'grid.width': (
        LINEWIDTH,
        validate._validate_pt,
        'Major gridline width. Alias for :rcraw:`grid.linewidth`.'
    ),
    'grid.widthratio': (
        GRIDRATIO,
        validate._validate_float,
        'Ratio of minor gridline width to major gridline width.'
    ),

    # Minor gridlines
    'gridminor': (
        False,
        validate._validate_bool,
        'Toggle minor gridlines on and off.'
    ),
    'gridminor.alpha': (
        GRIDALPHA,
        validate._validate_float,
        'Minor gridline opacity.'
    ),
    'gridminor.color': (
        BLACK,
        validate._validate_color,
        'Minor gridline color.'
    ),
    'gridminor.linestyle': (
        GRIDSTYLE,
        validate._validate_linestyle,
        'Minor gridline style.'
    ),
    'gridminor.linewidth': (
        GRIDRATIO * LINEWIDTH,
        validate._validate_pt,
        'Minor gridline width.'
    ),
    'gridminor.style': (
        GRIDSTYLE,
        validate._validate_linestyle,
        'Minor gridline style. Alias for :rcraw:`gridminor.linestyle`.'
    ),
    'gridminor.width': (
        GRIDRATIO * LINEWIDTH,
        validate._validate_pt,
        'Minor gridline width. Alias for :rcraw:`gridminor.linewidth`.'
    ),

    # Backend stuff
    'inlineformat': (
        'retina',
        validate._validate_belongs('svg', 'pdf', 'retina', 'png', 'jpeg'),
        'The inline backend figure format. Valid formats include '
        "``'svg'``, ``'pdf'``, ``'retina'``, ``'png'``, and ``jpeg``."
    ),

    # Inner borders
    'innerborders': (
        False,
        validate._validate_bool,
        'Toggles internal political border lines (e.g. states and provinces) '
        'on and off.'
    ),
    'innerborders.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for internal political border lines',
    ),
    'innerborders.color': (
        BLACK,
        validate._validate_color,
        'Line color for internal political border lines.'
    ),
    'innerborders.linewidth': (
        LINEWIDTH,
        validate._validate_pt,
        'Line width for internal political border lines.'
    ),
    'innerborders.zorder': (
        ZLINES,
        validate._validate_float,
        'Z-order for internal political border lines.'
    ),

    # Axis label settings
    'label.color': (
        BLACK,
        validate._validate_color,
        'Alias for :rcraw:`axes.labelcolor`.'
    ),
    'label.pad': (
        LABELPAD,
        validate._validate_pt,
        'Alias for :rcraw:`axes.labelpad`.'
        + _addendum_pt
    ),
    'label.size': (
        SMALLSIZE,
        validate._validate_fontsize,
        'Alias for :rcraw:`axes.labelsize`.' + _addendum_font
    ),
    'label.weight': (
        'normal',
        validate._validate_fontweight,
        'Alias for :rcraw:`axes.labelweight`.'
    ),

    # Lake patches
    'lakes': (
        False,
        validate._validate_bool,
        'Toggles lake patches on and off.'
    ),
    'lakes.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for lake patches',
    ),
    'lakes.color': (
        WHITE,
        validate._validate_color,
        'Face color for lake patches.'
    ),
    'lakes.zorder': (
        ZPATCHES,
        validate._validate_float,
        'Z-order for lake patches.'
    ),

    # Land patches
    'land': (
        False,
        validate._validate_bool,
        'Toggles land patches on and off.'
    ),
    'land.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for land patches',
    ),
    'land.color': (
        BLACK,
        validate._validate_color,
        'Face color for land patches.'
    ),
    'land.zorder': (
        ZPATCHES,
        validate._validate_float,
        'Z-order for land patches.'
    ),

    # Left subplot labels
    'leftlabel.color': (
        BLACK,
        validate._validate_color,
        'Font color for row labels on the left-hand side.'
    ),
    'leftlabel.pad': (
        TITLEPAD,
        validate._validate_pt,
        'Padding between axes content and row labels on the left-hand side.'
        + _addendum_pt
    ),
    'leftlabel.rotation': (
        'vertical',
        validate._validate_rotation,
        'Rotation for row labels on the left-hand side.' + _addendum_rotation
    ),
    'leftlabel.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'Font size for row labels on the left-hand side.' + _addendum_font
    ),
    'leftlabel.weight': (
        'bold',
        validate._validate_fontweight,
        'Font weight for row labels on the left-hand side.'
    ),

    # Meta settings
    'margin': (
        MARGIN,
        validate._validate_float,
        'The fractional *x* and *y* axis data margins when limits are unset. '
        'Alias for :rcraw:`axes.margin`.'
    ),
    'meta.edgecolor': (
        BLACK,
        validate._validate_color,
        'Color of axis spines, tick marks, tick labels, and labels.'
    ),
    'meta.color': (
        BLACK,
        validate._validate_color,
        'Color of axis spines, tick marks, tick labels, and labels. '
        'Alias for :rcraw:`meta.edgecolor`.'
    ),
    'meta.linewidth': (
        LINEWIDTH,
        validate._validate_pt,
        'Thickness of axis spines and major tick lines.'
    ),
    'meta.width': (
        LINEWIDTH,
        validate._validate_pt,
        'Thickness of axis spines and major tick lines. '
        'Alias for :rcraw:`meta.linewidth`.'
    ),

    # For negative positive patches
    'negcolor': (
        'blue7',
        validate._validate_color,
        'Color for negative bars and shaded areas when using ``negpos=True``. '
        'See also :rcraw:`poscolor`.'
    ),
    'poscolor': (
        'red7',
        validate._validate_color,
        'Color for positive bars and shaded areas when using ``negpos=True``. '
        'See also :rcraw:`negcolor`.'
    ),

    # Ocean patches
    'ocean': (
        False,
        validate._validate_bool,
        'Toggles ocean patches on and off.'
    ),
    'ocean.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for ocean patches',
    ),
    'ocean.color': (
        WHITE,
        validate._validate_color,
        'Face color for ocean patches.'
    ),
    'ocean.zorder': (
        ZPATCHES,
        validate._validate_float,
        'Z-order for ocean patches.'
    ),

    # Geographic resolution
    'reso': (
        'lo',
        validate._validate_belongs('lo', 'med', 'hi', 'x-hi', 'xx-hi'),
        'Resolution for `~proplot.axes.GeoAxes` geographic features. '
        "Must be one of ``'lo'``, ``'med'``, ``'hi'``, ``'x-hi'``, or ``'xx-hi'``."
    ),

    # Right subplot labels
    'rightlabel.color': (
        BLACK,
        validate._validate_color,
        'Font color for row labels on the right-hand side.'
    ),
    'rightlabel.pad': (
        TITLEPAD,
        validate._validate_pt,
        'Padding between axes content and row labels on the right-hand side.'
        + _addendum_pt
    ),
    'rightlabel.rotation': (
        'vertical',
        validate._validate_rotation,
        'Rotation for row labels on the right-hand side.' + _addendum_rotation
    ),
    'rightlabel.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'Font size for row labels on the right-hand side.' + _addendum_font
    ),
    'rightlabel.weight': (
        'bold',
        validate._validate_fontweight,
        'Font weight for row labels on the right-hand side.'
    ),

    # River lines
    'rivers': (
        False,
        validate._validate_bool,
        'Toggles river lines on and off.'
    ),
    'rivers.alpha': (
        None,
        validate._validate_or_none(validate._validate_float),
        'Opacity for river lines.',
    ),
    'rivers.color': (
        BLACK,
        validate._validate_color,
        'Line color for river lines.'
    ),
    'rivers.linewidth': (
        LINEWIDTH,
        validate._validate_pt,
        'Line width for river lines.'
    ),
    'rivers.zorder': (
        ZLINES,
        validate._validate_float,
        'Z-order for river lines.'
    ),

    # Subplots settings
    'subplots.align': (
        False,
        validate._validate_bool,
        'Whether to align axis labels during draw. See `aligning labels '
        '<https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html>`__.'  # noqa: E501
    ),
    'subplots.equalspace': (
        False,
        validate._validate_bool,
        'Whether to make the tight layout algorithm assign the same space for '
        'every row and the same space for every column.'
    ),
    'subplots.groupspace': (
        True,
        validate._validate_bool,
        'Whether to make the tight layout algorithm consider space between only '
        'adjacent subplot "groups" rather than every subplot in the row or column.'
    ),
    'subplots.innerpad': (
        1,
        validate._validate_em,
        'Padding between adjacent subplots.' + _addendum_em
    ),
    'subplots.outerpad': (
        0.5,
        validate._validate_em,
        'Padding around figure edge.' + _addendum_em
    ),
    'subplots.panelpad': (
        0.5,
        validate._validate_em,
        'Padding between subplots and panels, and between stacked panels.'
        + _addendum_em
    ),
    'subplots.panelwidth': (
        0.5,
        validate._validate_in,
        'Width of side panels.' + _addendum_in
    ),
    'subplots.refwidth': (
        2.5,
        validate._validate_in,
        'Default width of the reference subplot.' + _addendum_in
    ),
    'subplots.share': (
        True,
        validate._validate_belongs(0, 1, 2, 3, 4, False, 'labels', 'limits', True, 'all'),  # noqa: E501
        'The axis sharing level, one of ``0``, ``1``, ``2``, or ``3``, or the '
        "more intuitive aliases ``False``, ``'labels'``, ``'limits'``, or ``True``. "
        'See `~proplot.figure.Figure` for details.'
    ),
    'subplots.span': (
        True,
        validate._validate_bool,
        'Toggles spanning axis labels. See `~proplot.ui.subplots` for details.'
    ),
    'subplots.tight': (
        True,
        validate._validate_bool,
        'Whether to auto-adjust the subplot spaces and figure margins.'
    ),

    # Super title settings
    'suptitle.color': (
        BLACK,
        validate._validate_color,
        'Figure title color.'
    ),
    'suptitle.pad': (
        TITLEPAD,
        validate._validate_pt,
        'Padding between axes content and the figure super title.' + _addendum_pt
    ),
    'suptitle.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'Figure title font size.' + _addendum_font
    ),
    'suptitle.weight': (
        'bold',
        validate._validate_fontweight,
        'Figure title font weight.'
    ),

    # Tick settings
    'tick.color': (
        BLACK,
        validate._validate_color,
        'Major and minor tick color.'
    ),
    'tick.dir': (
        TICKDIR,
        validate._validate_belongs('in', 'out', 'inout'),
        'Major and minor tick direction. Must be one of '
        "``'out'``, ``'in'``, or ``'inout'``."
    ),
    'tick.labelcolor': (
        BLACK,
        validate._validate_color,
        'Axis tick label color.'
    ),
    'tick.labelpad': (
        TICKPAD,
        validate._validate_pt,
        'Padding between ticks and tick labels.' + _addendum_pt
    ),
    'tick.labelsize': (
        SMALLSIZE,
        validate._validate_fontsize,
        'Axis tick label font size.' + _addendum_font
    ),
    'tick.labelweight': (
        'normal',
        validate._validate_fontweight,
        'Axis tick label font weight.'
    ),
    'tick.len': (
        TICKLEN,
        validate._validate_pt,
        'Length of major ticks in points.'
    ),
    'tick.lenratio': (
        TICKLENRATIO,
        validate._validate_float,
        'Ratio of minor tickline length to major tickline length.'
    ),
    'tick.linewidth': (
        LINEWIDTH,
        validate._validate_pt,
        'Major tickline width.'
    ),
    'tick.minor': (
        TICKMINOR,
        validate._validate_bool,
        'Toggles minor ticks on and off.',
    ),
    'tick.pad': (
        TICKPAD,
        validate._validate_pt,
        'Alias for :rcraw:`tick.labelpad`.'
    ),
    'tick.width': (
        LINEWIDTH,
        validate._validate_pt,
        'Major tickline width. Alias for :rcraw:`tick.linewidth`.'
    ),
    'tick.widthratio': (
        TICKWIDTHRATIO,
        validate._validate_float,
        'Ratio of minor tickline width to major tickline width.'
    ),

    # Title settings
    'title.above': (
        True,
        validate._validate_belongs(False, True, 'panels'),
        'Whether to move outer titles and a-b-c labels above panels, colorbars, or '
        "legends that are above the axes. If the string 'panels' then text is only "
        'redirected above axes panels. Otherwise should be boolean.'
    ),
    'title.border': (
        True,
        validate._validate_bool,
        'Whether to draw a white border around titles '
        'when :rcraw:`title.loc` is inside the axes.'
    ),
    'title.borderwidth': (
        1.5,
        validate._validate_pt,
        'Width of the border around titles.'
    ),
    'title.bbox': (
        False,
        validate._validate_bool,
        'Whether to draw semi-transparent bounding boxes around titles '
        'when :rcraw:`title.loc` is inside the axes.'
    ),
    'title.bboxcolor': (
        WHITE,
        validate._validate_color,
        'Axes title bounding box color.'
    ),
    'title.bboxstyle': (
        'square',
        validate._validate_boxstyle,
        'Axes title bounding box style.'
    ),
    'title.bboxalpha': (
        0.5,
        validate._validate_float,
        'Axes title bounding box opacity.'
    ),
    'title.bboxpad': (
        None,
        validate._validate_or_none(validate._validate_pt),
        'Padding for the title bounding box. By default this is scaled '
        'to make the box flush against the axes edge.' + _addendum_pt
    ),
    'title.color': (
        BLACK,
        validate._validate_color,
        'Axes title color. Alias for :rcraw:`axes.titlecolor`.'
    ),
    'title.loc': (
        'center',
        functools.partial(validate._validate_loc, mode='text'),
        'Title position. For options see the :ref:`location table <title_table>`.'
    ),
    'title.pad': (
        TITLEPAD,
        validate._validate_pt,
        'Padding between the axes edge and the inner and outer titles and '
        'a-b-c labels. Alias for :rcraw:`axes.titlepad`.' + _addendum_pt
    ),
    'title.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'Axes title font size. Alias for :rcraw:`axes.titlesize`.' + _addendum_font
    ),
    'title.weight': (
        'normal',
        validate._validate_fontweight,
        'Axes title font weight. Alias for :rcraw:`axes.titleweight`.'
    ),

    # Top subplot label settings
    'toplabel.color': (
        BLACK,
        validate._validate_color,
        'Font color for column labels on the top of the figure.'
    ),
    'toplabel.pad': (
        TITLEPAD,
        validate._validate_pt,
        'Padding between axes content and column labels on the top of the figure.'
        + _addendum_pt
    ),
    'toplabel.rotation': (
        'horizontal',
        validate._validate_rotation,
        'Rotation for column labels at the top of the figure.' + _addendum_rotation
    ),
    'toplabel.size': (
        LARGESIZE,
        validate._validate_fontsize,
        'Font size for column labels on the top of the figure.' + _addendum_font
    ),
    'toplabel.weight': (
        'bold',
        validate._validate_fontweight,
        'Font weight for column labels on the top of the figure.'
    ),

    # Unit formatting
    'unitformat': (
        'L',
        validate._validate_string,
        'The format string used to format `pint.Quantity` default unit labels '
        'using ``format(units, unitformat)``. See also :rcraw:`autoformat`.'
    ),
}

# Child settings. Changing the parent changes all the children, but
# changing any of the children does not change the parent.
_rc_children = {
    'font.smallsize': (  # the 'small' fonts
        'tick.labelsize', 'xtick.labelsize', 'ytick.labelsize',
        'axes.labelsize', 'legend.fontsize', 'grid.labelsize'
    ),
    'font.largesize': (  # the 'large' fonts
        'abc.size', 'figure.titlesize', 'suptitle.size', 'axes.titlesize', 'title.size',
        'leftlabel.size', 'toplabel.size', 'rightlabel.size', 'bottomlabel.size'
    ),
    'meta.color': (  # change the 'color' of an axes
        'axes.edgecolor', 'axes.labelcolor', 'legend.edgecolor', 'colorbar.edgecolor',
        'tick.labelcolor', 'hatch.color', 'xtick.color', 'ytick.color'
    ),
    'meta.width': (  # change the tick and frame line width
        'axes.linewidth', 'tick.width', 'tick.linewidth', 'xtick.major.width',
        'ytick.major.width', 'grid.width', 'grid.linewidth',
    ),
    'axes.margin': ('axes.xmargin', 'axes.ymargin'),
    'grid.color': ('gridminor.color', 'grid.labelcolor'),
    'grid.alpha': ('gridminor.alpha',),
    'grid.linewidth': ('gridminor.linewidth',),
    'grid.linestyle': ('gridminor.linestyle',),
    'tick.color': ('xtick.color', 'ytick.color'),
    'tick.dir': ('xtick.direction', 'ytick.direction'),
    'tick.len': ('xtick.major.size', 'ytick.major.size'),
    'tick.minor': ('xtick.minor.visible', 'ytick.minor.visible'),
    'tick.pad': ('xtick.major.pad', 'xtick.minor.pad', 'ytick.major.pad', 'ytick.minor.pad'),  # noqa: E501
    'tick.width': ('xtick.major.width', 'ytick.major.width'),
    'tick.labelsize': ('xtick.labelsize', 'ytick.labelsize'),
}

# Recently added settings. Update these only if the version is recent enough
# NOTE: We don't make 'title.color' a child of 'axes.titlecolor' because
# the latter can take on the value 'auto' and can't handle that right now.
if 'mathtext.fallback' in _rc_matplotlib_default:
    _rc_matplotlib_override['mathtext.fallback'] = 'stixsans'
if 'axes.titlecolor' in _rc_matplotlib_default:  # matplotlib >= 3.2
    _rc_children['title.color'] = ('axes.titlecolor',)
    _rc_matplotlib_override['axes.titlecolor'] = BLACK
if 'xtick.labelcolor' in _rc_matplotlib_default:  # matplotlib >= 3.4
    _rc_children['tick.labelcolor'] = ('xtick.labelcolor', 'ytick.labelcolor')
    _rc_children['grid.labelcolor'] = ('xtick.labelcolor', 'ytick.labelcolor')
    _rc_children['meta.color'] += ('xtick.labelcolor', 'ytick.labelcolor')
    _rc_matplotlib_override['xtick.labelcolor'] = BLACK
    _rc_matplotlib_override['ytick.labelcolor'] = BLACK

# Setting synonyms. Changing one setting changes the other. Also account for existing
# children. Most of these are aliased due to proplot settings overlapping with
# existing matplotlib settings.
_rc_synonyms = (
    ('cmap', 'image.cmap', 'cmap.sequential'),
    ('cmap.lut', 'image.lut'),
    ('font.name', 'font.family'),
    ('font.small', 'font.smallsize'),
    ('font.large', 'font.largesize'),
    ('formatter.limits', 'axes.formatter.limits'),
    ('formatter.use_locale', 'axes.formatter.use_locale'),
    ('formatter.use_mathtext', 'axes.formatter.use_mathtext'),
    ('formatter.min_exponent', 'axes.formatter.min_exponent'),
    ('formatter.use_offset', 'axes.formatter.useoffset'),
    ('formatter.offset_threshold', 'axes.formatter.offset_threshold'),
    ('grid.below', 'axes.axisbelow'),
    ('grid.labelpad', 'grid.pad'),
    ('grid.linewidth', 'grid.width'),
    ('grid.linestyle', 'grid.style'),
    ('gridminor.linewidth', 'gridminor.width'),
    ('gridminor.linestyle', 'gridminor.style'),
    ('label.color', 'axes.labelcolor'),
    ('label.pad', 'axes.labelpad'),
    ('label.size', 'axes.labelsize'),
    ('label.weight', 'axes.labelweight'),
    ('margin', 'axes.margin'),
    ('meta.width', 'meta.linewidth'),
    ('meta.color', 'meta.edgecolor'),
    ('tick.labelpad', 'tick.pad'),
    ('tick.labelsize', 'grid.labelsize'),
    ('tick.labelcolor', 'grid.labelcolor'),
    ('tick.labelweight', 'grid.labelweight'),
    ('tick.linewidth', 'tick.width'),
    ('title.pad', 'axes.titlepad'),
    ('title.size', 'axes.titlesize'),
    ('title.weight', 'axes.titleweight'),
)
for _keys in _rc_synonyms:
    for _key in _keys:
        _set = {_ for k in _keys for _ in {k, *_rc_children.get(k, ())}} - {_key}
        _rc_children[_key] = tuple(sorted(_set))

# Previously removed settings.
# NOTE: Initial idea was to defer deprecation warnings in Configurator to the
# subsequent RcParams indexing. However this turned out be complicated, because
# would have to detect deprecated keys in _get_item_dicts blocks, and need to
# validate values before e.g. applying 'tick.lenratio'. So the renamed parameters
# do not have to be added as _rc_children, since Configurator translates before
# retrieving the list of children in _get_item_dicts.
_rc_proplot_removed = {  # {key: (alternative, version)} dictionary
    'rgbcycle': ('', '0.6.0'),  # no alternative, we no longer offer this feature
    'geogrid.latmax': ('Please use ax.format(latmax=N) instead.', '0.6.0'),
    'geogrid.latstep': ('Please use ax.format(latlines=N) instead.', '0.6.0'),
    'geogrid.lonstep': ('Please use ax.format(lonlines=N) instead.', '0.6.0'),
    'gridminor.latstep': ('Please use ax.format(latminorlines=N) instead.', '0.6.0'),
    'gridminor.lonstep': ('Please use ax.format(lonminorlines=N) instead.', '0.6.0'),
}
_rc_proplot_renamed = {  # {old_key: (new_key, version)} dictionary
    'abc.format': ('abc', '0.5.0'),
    'align': ('subplots.align', '0.6.0'),
    'axes.facealpha': ('axes.alpha', '0.6.0'),
    'geoaxes.edgecolor': ('axes.edgecolor', '0.6.0'),
    'geoaxes.facealpha': ('axes.alpha', '0.6.0'),
    'geoaxes.facecolor': ('axes.facecolor', '0.6.0'),
    'geoaxes.linewidth': ('axes.linewidth', '0.6.0'),
    'geogrid.alpha': ('grid.alpha', '0.6.0'),
    'geogrid.color': ('grid.color', '0.6.0'),
    'geogrid.labels': ('grid.labels', '0.6.0'),
    'geogrid.labelpad': ('grid.pad', '0.6.0'),
    'geogrid.labelsize': ('grid.labelsize', '0.6.0'),
    'geogrid.linestyle': ('grid.linestyle', '0.6.0'),
    'geogrid.linewidth': ('grid.linewidth', '0.6.0'),
    'share': ('subplots.share', '0.6.0'),
    'small': ('font.smallsize', '0.6.0'),
    'large': ('font.largesize', '0.6.0'),
    'span': ('subplots.span', '0.6.0'),
    'tight': ('subplots.tight', '0.6.0'),
    'axes.formatter.timerotation': ('formatter.timerotation', '0.6.0'),
    'axes.formatter.zerotrim': ('formatter.zerotrim', '0.6.0'),
    'abovetop': ('title.above', '0.7.0'),
    'subplots.pad': ('subplots.outerpad', '0.7.0'),
    'subplots.axpad': ('subplots.innerpad', '0.7.0'),
    'subplots.axwidth': ('subplots.refwidth', '0.7.0'),
    'text.labelsize': ('font.smallsize', '0.8.0'),
    'text.titlesize': ('font.largesize', '0.8.0'),
    'alpha': ('axes.alpha', '0.8.0'),
    'facecolor': ('axes.facecolor', '0.8.0'),
    'edgecolor': ('meta.color', '0.8.0'),
    'color': ('meta.color', '0.8.0'),
    'linewidth': ('meta.width', '0.8.0'),
    'lut': ('cmap.lut', '0.8.0'),
    'image.levels': ('cmap.levels', '0.8.0'),
    'image.inbounds': ('cmap.inbounds', '0.8.0'),
    'image.discrete': ('cmap.discrete', '0.8.0'),
    'image.edgefix': ('edgefix', '0.8.0'),
    'tick.ratio': ('tick.widthratio', '0.8.0'),
    'grid.ratio': ('grid.widthratio', '0.8.0'),
    'abc.style': ('abc', '0.8.0'),
    'grid.loninline': ('grid.inlinelabels', '0.8.0'),
    'grid.latinline': ('grid.inlinelabels', '0.8.0'),
    'cmap.edgefix': ('edgefix', '0.9.0'),
    'basemap': ('geo.backend', '0.10.0'),
    'inlinefmt': ('inlineformat', '0.10.0'),
    'cartopy.circular': ('geo.round', '0.10.0'),
    'cartopy.autoextent': ('geo.extent', '0.10.0'),
    'colorbar.rasterize': ('colorbar.rasterized', '0.10.0'),
}
